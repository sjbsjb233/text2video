import time
from script import database
from script import chatgpt


def generate_answer(question, system=False, engine='gpt-3.5-turbo'):
    '''生成sd_prompt'''
    if system == False:
        # 从数据库中获取chatgpt_system_default
        sql = '''SELECT chatgpt_system_default FROM setting WHERE id=1'''
        system = database.select_data(
            sql, (), 'data/setting.db')[0][0]

    # 生成prompt
    answer, total_tokens,response = chatgpt.generate_answer(question, system, engine)

    return answer, total_tokens,response


def gpt_queue(path: str):
    '''本函数提供给多进程监听gpt_queue数据库使用'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'

    # 循环监听数据库gpt_queue的数据
    while True:
        # 查询gpt_queue表中的数据，state=2的数据，优先用operate降序,其次用id来升序排序
        #优先进行智能分镜
        sql = '''SELECT id,main_id,operate,prompt FROM gpt_queue WHERE state=2 ORDER BY operate DESC,id ASC'''
        data = database.select_data(sql, (), '%stemperature.db' % path)
        if data:
            # 如果没有数据
            time.sleep(1)
            continue

        # 如果有数据
        data = data[0]

        # 将其state更新为3
        sql1 = '''UPDATE gpt_queue SET state=3 WHERE id=?'''
        database.change_data(sql1, (data[0],), '%stemperature.db' % path)

        # 获取text
        text = data[3]

        #从setting表中获取预设的system
        if data[2] == 0:
            # 如果operate为0，从setting表中获取chatgpt_system_default
            sql = '''SELECT chatgpt_system_default FROM setting WHERE id=1'''
            system = database.select_data(
                sql, (), '%stemperature.db' % path)[0][0]
        elif data[2] == 1:
            # 如果operate为1，从setting表中获取chatgpt_split_system
            sql = '''SELECT chatgpt_split_system FROM setting WHERE id=1'''
            system = database.select_data(
                sql, (), '%stemperature.db' % path)[0][0]

        # 生成prompt
        answer, acutal_tokens,response = generate_answer(text, system)

        if answer:
            # 将answer,acutal_tokens和response写入gpt_queue表中
            sql = '''UPDATE gpt_queue SET completion=?,acutal_tokens=?,response=? WHERE id=?'''
            database.change_data(sql, (answer, acutal_tokens,str(response), data[0]),
                                    '%stemperature.db' % path)
            
            # 将其state更新为4
            sql = '''UPDATE gpt_queue SET state=4 WHERE id=?'''
            database.change_data(sql, (data[0],), '%stemperature.db' % path)
            
        else:
            # 将其state更新为1
            sql = '''UPDATE gpt_queue SET state=1 WHERE id=?'''
            database.change_data(sql, (data[0],), '%stemperature.db' % path)


if __name__ == '__main__':
    a = generate_answer('你是谁', system='')
    print(a)

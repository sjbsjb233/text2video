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
    answer, total_tokens, response = chatgpt.generate_answer(
        question, system, engine)

    return answer, total_tokens, response


def gpt_prompt(path: str, main_id: int):
    '''将main表text内容使用chatgpt生成prompt'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'
    # 获取main表中的text
    sql = '''SELECT text FROM main WHERE id=?'''
    text = database.select_data(
        sql, (main_id,), '%stemperature.db' % path)[0][0]

    # 向gpt_queue表中加入数据,并获取刚刚插入的id
    sql = '''INSERT INTO gpt_queue (main_id,prompt,state,operate) VALUES (?,?,2,0)'''
    database.change_data(sql, (main_id, text), '%stemperature.db' % path)
    sql = '''SELECT id FROM gpt_queue WHERE main_id=? AND prompt=? AND state=2 AND operate=0 ORDER BY id DESC'''
    id = database.select_data(sql, (main_id, text),
                              '%stemperature.db' % path)[0][0]

    # 将main表中的prompt_id更新为该id
    sql = '''UPDATE main SET prompt_id=? WHERE id=?'''
    database.change_data(sql, (id, main_id), '%stemperature.db' % path)

    return True


def gpt_change_prompt(path: str, main_id: int):
    '''chatgpt生成的prompt不符合要求,重新生成'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'

    # 清除main表中prompt_id的数据
    sql = '''UPDATE main SET prompt_id=NULL WHERE id=?'''
    database.change_data(sql, (main_id,), '%stemperature.db' % path)

    # 重新生成
    gpt_prompt(path, main_id)


def gpt_queue(path: str):
    '''本函数提供给多进程监听gpt_queue数据库使用'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'

    # 循环监听数据库gpt_queue的数据
    while True:
        # 查询gpt_queue表中的数据，state=2的数据，优先用operate降序,其次用id来升序排序
        # 优先进行智能分镜
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

        # 从setting表中获取预设的system
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
        answer, acutal_tokens, response = generate_answer(text, system)

        if answer:
            # 将answer,acutal_tokens和response写入gpt_queue表中
            sql = '''UPDATE gpt_queue SET completion=?,acutal_tokens=?,response=? WHERE id=?'''
            database.change_data(sql, (answer, acutal_tokens, str(response), data[0]),
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

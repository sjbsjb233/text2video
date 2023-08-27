import json
import re
import time
import tiktoken
from script import database
from script import chatgpt

'''
    分割文本到列表中
'''


def cut_novel(path, target_path, persent: object, regex=r'\s==.+==', delete_str_regex=None):
    '''机械化按章节分割文本'''
    # 检测文件是否存在
    try:
        with open(path, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        print('文件不存在')
        return False

    # 检测target_path是否加上/
    if target_path[-1] != '/':
        target_path += '/'

    # 读取文本
    with open(path, 'r', encoding='utf-8') as f:
        novel = f.read()
    # 若delete_str_regex有内容,则删除不需要的字符串(正则表达式)
    if delete_str_regex:
        novel = re.sub(delete_str_regex, '', novel)

    # 分割文本
    chapter_list = re.split(regex, novel)

    # 去除空白章节
    chapter_list = [chapter for chapter in chapter_list if chapter != '']
    # 去除列表中非字符串元素
    chapter_list = [
        chapter for chapter in chapter_list if isinstance(chapter, str)]

    # 在tarrget_path中的数据库写入分割后的章节
    chapter_index = 1
    for chapter in chapter_list:
        chapter_content = chapter.strip()
        # 写入数据库
        sql = '''
        INSERT INTO original_content(chapter,text) VALUES(?, ?)'''
        database.change_data(
            sql, (chapter_index, chapter_content), '%stemperature.db' % target_path)
        chapter_index += 1
        # 计算进度
        persent.setValue(round(chapter_index/len(chapter_list)*100))
    persent.setValue(100)
    return True


def cut_novel_human(text: str, path: str, chapter: int):
    '''人工分割文本
    text:分割后的文本(使用\\n分割文本)
    chapter:当前操作的章节
    path:数据库路径
    '''
    # 检查path结尾是否为/
    if path[-1] != '/':
        path += '/'

    # 分割文本
    original_content_list = text.split('\n')

    # 删除异常行
    original_content_list = [line for line in original_content_list if line != '' and line !=
                             ' ' and line != '\n' and line != '\t' and line != '\r' and line != '\r\n'
                             and line != '\n\r' and line != '\r\n\r\n']

    # 将分割后的原文写入数据库
    for chapter_index in range(len(original_content_list)):
        chapter_content = original_content_list[chapter_index]
        chapter_part = chapter_index+1

        # 从setting表中获取chatgpt_system_default
        sql = '''SELECT chatgpt_system_default FROM setting WHERE id=1'''
        chatgpt_system_default = database.select_data(
            sql, (), 'data/setting.db')[0][0]

        sql = '''
        INSERT INTO main(chapter,part,text) VALUES(?, ?, ?)'''
        database.change_data(
            sql, (chapter, chapter_part, chapter_content), '%stemperature.db' % path)


def gpt_split(path: str, chapters: list,persent: object):
    '''ChatGPT分割文本,将任务加入gpt_queue表的队列中
    chapters:需要分割的章节列表'''
    # 检查path结尾是否为/
    if path[-1] != '/':
        path += '/'

    # 从setting表中获取chatgpt_max_tokens和chatgpt_split_system
    sql = '''SELECT chatgpt_max_tokens,chatgpt_split_system FROM setting WHERE id=1'''
    data = database.select_data(sql, (), 'data/setting.db')[0]
    chatgpt_max_tokens, chatgpt_split_system = data[0], data[1]

    for chapter in chapters:
        split_chapter = chapter.split('\n')
        # 删除异常行
        original_content_list = [line for line in original_content_list if line != '' and line !=
                                 ' ' and line != '\n' and line != '\t' and line != '\r' and line != '\r\n'
                                 and line != '\n\r' and line != '\r\n\r\n']

        # 框取小于chatgpt_max_tokens的最大文本的tokens
        content_list = []
        start = 0
        flag = True
        for i in range(len(split_chapter)):
            now_spend_tokens = chatgpt.num_tokens_from_string(
                "\n".join(split_chapter[start:i+1]), chatgpt_split_system)
            if now_spend_tokens > chatgpt_max_tokens:
                if i-start == 0:
                    # 如果一句话分的太长,则直接报错
                    return False
                prompt = "\n".join(split_chapter[start:i])

                content_list.append(prompt)
                start = i
                flag = False

        if flag:
            # 整篇文章一次就能分镜完
            prompt = "\n".join(split_chapter)
            content_list.append(prompt)

        # 将content_list中的内容加入gpt_queue表的队列中，并获取该任务的id
        finally_result = []
        for prompt in content_list:
            now_spend_tokens = chatgpt.num_tokens_from_string(
                prompt, chatgpt_split_system)
            sql1 = '''
            INSERT INTO gpt_queue(operate,state,main_id,prompt,expected_tokens) VALUES(?,?,-1,?,?)'''
            sql2 = '''
            SELECT id FROM gpt_queue WHERE operate=? AND state=? AND main_id=? AND prompt=? AND expected_tokens=?'''
            database.change_data(
                sql1, (1, 2, prompt, now_spend_tokens))
            gpt_queue_id = database.select_data(
                sql2, (1, 2, -1, prompt, now_spend_tokens))[0][0]

            # 监听该任务的状态,直到状态变为4
            while True:
                sql = '''
                SELECT state FROM gpt_queue WHERE id=?'''
                state = database.select_data(sql, (gpt_queue_id,))[0][0]
                if state == 2 or state == 3:
                    time.sleep(0.7)
                    continue
                elif state == 1 or state == 5:
                    # 任务失败或者被取消
                    return False

                # 读取生成的文本
                sql = '''
                SELECT completion FROM gpt_queue WHERE id=?'''
                completion = database.select_data(sql, (gpt_queue_id,))[0][0]

                # completion是json格式的，格式为：{"part1":"[内容1]","part2":"[内容2]",...}
                # 提取出completion中的内容，并将其按照part排序append到finally_result中
                completion = json.loads(completion)
                for i in range(len(completion)):
                    finally_result.append(completion["part"+str(i+1)])
                break
            # 计算进度(不精准)
            persent.setValue(round(len(finally_result)/(len(content_list)*2.5)*100))
    persent.setValue(100)

    return finally_result


if __name__ == '__main__':
    if cut_novel(r'novel/我不想继承万亿家产.txt', r'temp\novel', r'===.+?===', r'\n\n    我不想继承万亿家产(\n\n)?'):
        print('分割成功')

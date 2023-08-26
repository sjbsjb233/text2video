'''操作数据库的模块，与数据库对接'''
import sqlite3
import os
import datetime
import re
from script import database


def create_orginal_table(path):
    '''创建项目原始的空表，项目开始时使用'''
    # 判定path是否加上/
    if path[-1] != '/':
        path += '/'

    # 创建数据库
    conn = sqlite3.connect("%stemperature.db" % path)

    # 写入新表
    c = conn.cursor()

    # 小说文本内容的表（原始内容，未经加工）
    c.execute('''CREATE TABLE original_content(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              chapter INT NOT NULL,
              text TEXT NOT NULL)
              ''')

    # 小说文本内容的表（经过加工后的内容,主项目表）
    c.execute('''CREATE TABLE main(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              chapter INT NOT NULL,
              part INT NOT NULL,
              text TEXT NOT NULL,
              prompt_id TEXT NULL,
              pic_id INT NULL,
              tts_id INT NULL,
              hire_fix_id INT NULL
              )''')
    # 状态state定义：0：未处理，1：异常，2：排队中，3：处理中，4：处理完成 ,5:暂停

    # sd排队队列
    c.execute('''CREATE TABLE sd_queue(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              operate TINYINT NOT NULL,
              state TINYINT NOT NULL DEFAULT 2,
              main_id INT NOT NULL,
              path TEXT NOT NULL,
              api_rep TEXT NULL
              )''')
    # operate定义：0：text2img，1：hires_fix，2：动图生成

    # chatgpt排队队列
    c.execute('''CREATE TABLE gpt_queue(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              operate TINYINT NOT NULL,
              state TINYINT NOT NULL DEFAULT 2,
              main_id INT NOT NULL,
              prompt TEXT NOT NULL,
              completion TEXT NULL,
              response TEXT NULL,
              expect_tokens NULL,
              actual_tokens NULL
              )''')

    # 配音排队队列
    c.execute('''CREATE TABLE tts_queue(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              state TINYINT NOT NULL DEFAULT 2,
              main_id INT NOT NULL,
              tts_path TEXT NULL,
              tts_speeed FLOAT NOT NULL DEFAULT 1.0,
              tts_voice TEXT NOT NULL
              )''')

    # 人格固定
    c.execute('''CREATE TABLE figure(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name1 TEXT NOT NULL,
                name2 TEXT NULL,
                name3 TEXT NULL,
                lora TEXT NULL,
                prompt TEXT NULL
                )''')

    conn.commit()
    conn.close()


def make_dir(path):
    '''创建项目临时处理文件夹'''

    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'

    if not os.path.exists(path):
        os.makedirs(path)

    # 创建子目录sound和pic
    if not os.path.exists(path + 'sound'):
        os.makedirs(path + 'sound')
    if not os.path.exists(path + 'pic'):
        os.makedirs(path + 'pic')


def insert_dominate(name: str, cut_novel: bool, cut_re: str, novel_path: str, present: object):
    '''将项目信息写入dominate表'''

    # 获取当前时间
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")

    # 写入dominate表
    conn = sqlite3.connect("data/database.db")
    c = conn.cursor()
    c.execute('''INSERT INTO dominate(name,create_time,tokens,step,path) VALUES(?,?,?,?,?)''',
              (name, now, 0, 0, "temp/%s" % name))
    conn.commit()
    conn.close()

    # 创建项目文件夹
    make_dir("temp/%s" % name)

    # 创建项目原始表
    create_orginal_table("temp/%s" % name)

    path = "temp/%s/" % name

    with open(novel_path, 'r', encoding='utf-8') as f:
        novel = f.read()
    # 将小说内容写入original_content表
    if cut_novel:
        # 读取小说内容
        # 切割小说(正则表达式为切割标准,cut_re)
        novel = re.split(cut_re, novel)
        # 将小说内容写入original_content表
        conn = sqlite3.connect("%stemperature.db" % path)
        c = conn.cursor()
        for i in range(len(novel)):
            c.execute('''INSERT INTO original_content(chapter,text) VALUES(?,?)''',
                      (i+1, novel[i]))
            # 计算进度
            present.setValue(round(i/len(novel)*100))
        present.setValue(100)
        conn.commit()
        conn.close()
    else:
        # 将小说内容写入original_content表
        conn = sqlite3.connect("%stemperature.db" % path)
        c = conn.cursor()
        c.execute('''INSERT INTO original_content(chapter,text) VALUES(?,?)''',
                  (1, novel))
        present.setValue(100)
        conn.commit()
        conn.close()


def get_dominate(id=-1):
    '''获取dominate表中的数据'''
    if id == -1:
        conn = sqlite3.connect("data/database.db")
        c = conn.cursor()
        c.execute('''SELECT * FROM dominate''')
        data = c.fetchall()
        conn.commit()
        conn.close()
        return data
    else:
        conn = sqlite3.connect("data/database.db")
        c = conn.cursor()
        c.execute('''SELECT * FROM dominate WHERE id=?''', (id,))
        data = c.fetchall()
        conn.commit()
        conn.close()
        return data


def if_project_name_exist(name):
    '''判定项目名称是否已存在'''
    data = database.select_data(
        '''SELECT * FROM dominate WHERE name=?''', (name,), r'data\database.db')
    flag = False
    for i in data:
        if i[1] == name:
            flag = True
            break
    return flag


def get_program_info(dominate_id):
    '''获取指定项目的信息'''
    data = database.select_data(
        '''SELECT * FROM dominate WHERE id=?''', (dominate_id,), r'data\database.db')
    return data[0]


def delete_program_dir(dominate_id):
    '''删除指定项目'''
    # 删除项目文件夹
    path = get_program_info(dominate_id)[-1]+'/'
    os.remove(path+'temperature.db')
    os.rmdir(path+'sound')
    os.rmdir(path+'pic')
    os.rmdir(path)
    # dominate表中删除该行数据
    database.change_data('''DELETE FROM dominate WHERE id=?''',
                         (dominate_id,), r'data\database.db')

def update_dominate_name(dominate_id, name):
    '''更新dominate表中的name'''
    database.change_data('''UPDATE dominate SET name=? WHERE id=?''',
                         (name, dominate_id), r'data\database.db')

if __name__ == '__main__':
    create_orginal_table(r'temp\novel')
    make_dir(r'temp\novel')

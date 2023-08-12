'''操作数据库的模块，与数据库对接'''
import sqlite3,os
import datetime
import time


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

    #sd排队队列
    c.execute('''CREATE TABLE sd_queue(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              operate TINYINT NOT NULL,
              state TINYINT NOT NULL DEFAULT 2,
              main_id INT NOT NULL,
              path TEXT NOT NULL,
              api_rep TEXT NULL
              )''')
    # operate定义：0：text2img，1：hires_fix，2：动图生成

    #chatgpt排队队列
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
    
    #配音排队队列
    c.execute('''CREATE TABLE tts_queue(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              state TINYINT NOT NULL DEFAULT 2,
              main_id INT NOT NULL,
              tts_path TEXT NULL,
              tts_speeed FLOAT NOT NULL DEFAULT 1.0,
              tts_voice TEXT NOT NULL
              )''')
    
    #人格固定
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
    
    #检查path是否加上/
    if path[-1] != '/':
        path += '/'

    if not os.path.exists(path):
        os.makedirs(path)
    
    #创建子目录sound和pic
    if not os.path.exists(path + 'sound'):
        os.makedirs(path + 'sound')
    if not os.path.exists(path + 'pic'):
        os.makedirs(path + 'pic')
    
if __name__ == '__main__':
    create_orginal_table(r'temp\novel')
    make_dir(r'temp\novel')
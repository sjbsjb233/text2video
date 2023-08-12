import sqlite3


def select_data(sql, optional, path):
    """查询数据"""
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(sql, optional)
    data = c.fetchall()
    conn.close()
    return data


def change_data(sql, optional, path):
    """修改数据"""
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(sql, optional)
    conn.commit()
    conn.close()


def select_data_more(sqls: tuple, optionals: tuple, path: str):
    '''查询多条数据
    '''
    conn = sqlite3.connect(path)
    c = conn.cursor()
    data = []
    for sql, optional in zip(sqls, optionals):
        c.execute(sql, optional)
        data.append(c.fetchall())
    conn.close()
    return data


def change_data_more(sqls: tuple, optionals: tuple, path: str):
    '''修改多条数据
    '''
    conn = sqlite3.connect(path)
    c = conn.cursor()
    for sql, optional in zip(sqls, optionals):
        c.execute(sql, optional)
    conn.commit()
    conn.close()

def select_change_data(sqls: tuple, optionals: tuple, path: str):
    '''查询多条数据并修改多条数据
    '''
    conn = sqlite3.connect(path)
    c = conn.cursor()
    data = []
    for sql, optional in zip(sqls, optionals):
        c.execute(sql, optional)
        data.append(c.fetchall())
    conn.commit()
    conn.close()
    return data
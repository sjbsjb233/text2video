import asyncio
import time
import edge_tts
from script import database


async def _main(text, path, voice, speed=1) -> None:
    speed -= 1
    if speed < 0:
        speed = "-%s%" % abs(speed)
    elif speed > 0:
        speed = "+%s%" % abs(speed)
    else:
        speed = "+0%"
    communicate = edge_tts.Communicate(text, voice, rate=speed)
    await communicate.save(path)


def tts(text, path, voice="zh-CN-YunxiNeural"):
    '''文本转语音Edge TTS'''
    try:
        asyncio.run(_main(text, path, voice))
    except:
        return False
    return True


def tts_queue(path: str):
    '''本函数提供给多进程监听tts_queue数据库使用'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'

    # 循环监听数据库tts_queue的数据
    while True:
        # 查询tts_queue表中的数据，state=2的数据，用id来升序排序
        sql = '''SELECT id,main_id,tts_speed,tts_voice FROM tts_queue WHERE state=2 ORDER BY id ASC'''
        data = database.select_data(sql, (), '%stemperature.db' % path)

        if not data:
            # 如果没有数据，休眠1秒
            time.sleep(1)
            continue

        # 如果有数据
        data = data[0]

        # 将其state更新为3(处理中)
        sql1 = '''UPDATE tts_queue SET state=3 WHERE id=?'''
        database.change_data(sql1, (data[0],), '%stemperature.db' % path)

        tts_speed=data[2]
        voice = data[3]

        # 从main表中获取text
        sql = '''SELECT text FROM main WHERE id=?'''
        text = database.select_data(
            sql, (data[1],), '%stemperature.db' % path)[0][0]

        # tts操作
        if tts(text, '%ssound/%s.mp3' % (path, data[0]), voice, tts_speed):
            # 将tts生成的文件路径写入tts_queue表,并将其state更新为4(完成)
            sql = '''UPDATE tts_queue SET completion=?,state=4 WHERE id=?'''
            database.change_data(
                sql, ('%ssound/%s.mp3' % (path, data[0]), data[0]), '%stemperature.db' % path)

        else:
            # 将其state更新为1（异常）
            sql = '''UPDATE tts_queue SET state=1 WHERE id=?'''
            database.change_data(sql, (data[0],), '%stemperature.db' % path)




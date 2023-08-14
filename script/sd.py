# from script import database
import time
import database
import webuiapi
from PIL import Image


api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)


def text2img(prompt: str, save_path: str, negative_prompt: str = '', seed: int = -1,
             cfg_scale: int = 7, sampler_name: str = 'DPM++ 2S a Karras',
             width: int = 768, height: int = 512, steps: int = 20,
             enable_hr: bool = False, restore_faces: bool = True):
    '''文本转图像'''
    # 从数据库setting表中获取sd_prompt,sd_negative_prompt,sd_seed,sd_cfg_scale,sd_sampler_name,sd_width,sd_height,sd_steps,sd_restore_faces
    sql = '''SELECT sd_prompt,sd_negative_prompt,sd_seed,sd_cfg_scale,sd_sampler_name,sd_width,sd_height,sd_steps,sd_restore_faces FROM setting WHERE id=1'''
    data = database.select_data(sql, (), 'data/setting.db')[0]
    try:
        result = api.txt2img(prompt="%s,%s" % (data[0], prompt), negative_prompt=data[1], seed=data[2], cfg_scale=data[3],
                             sampler_name=data[4], width=data[5], height=data[6], steps=data[7], enable_hr=enable_hr, restore_faces=data[8])
        result.image.save(save_path)
    except:
        return False
    return result.info


def hires_fix(path: str, save_path: str):
    '''修复高分辨率图像'''
    # 从数据库setting表中获取sd_upscaler_1,,sd_upscaling_resize
    sql = '''SELECT sd_upscaler_1,sd_upscaling_resize FROM setting WHERE id=1'''
    data = database.select_data(sql, (), 'data/setting.db')[0]
    try:
        pic = Image.open(path)
        result = api.extra_single_image(
            image=pic, upscaler_1=data[0], upscaling_resize=data[1])
        result.image.save(save_path)
    except:
        return False
    return result.info

def sd_queue(path):
    '''本函数提供给多进程监听sd_queue数据库使用'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'
    # 循环监听数据库sd_queue的数据
    while True:
        # 查询sd_queue表中的数据，state=2的数据，用id来升序排序
        sql = '''SELECT id,main_id,operate FROM sd_queue WHERE state=2 ORDER BY id ASC'''
        data = database.select_data(sql, (), '%stemperature.db' % path)
        if not data:
            # 如果没有数据，休眠1秒
            time.sleep(1)
            continue
        # 如果有数据
        data = data[0]
        # 将其state更新为3(处理中)
        sql1 = '''UPDATE sd_queue SET state=3 WHERE id=?'''
        database.change_data(sql1, (data[0],), '%stemperature.db' % path)
        #确认operate操作模式
        if data[2] == 0:
            # 从gpt_queue表中获取completion(main表中的prompt_id为gpt_queue表中的id)

            sql = '''SELECT prompt_id FROM main WHERE id=?'''
            prompt_id = database.select_data(
                sql, (data[1],), '%stemperature.db' % path)[0][0]
            sql='''SELECT completion FROM gpt_queue WHERE id=?'''
            completion=database.select_data(
                sql, (prompt_id,), '%stemperature.db' % path)[0][0]
            # sd操作
            api_rep=text2img(completion, '%simage/%s.png' % (path, data[0]))
            # 将sd生成的文件路径写入sd_queue表,并将其state更新为4(完成)
            sql2 = '''UPDATE sd_queue SET path=?,state=4 WHERE id=?'''
            database.change_data(
                sql2, ('%simage/%s.png' % (path, data[0]), data[0]), '%stemperature.db' % path)

if __name__ == '__main__':
    print(text2img('masterpiece,4k,(beautiful face),1girl,white background', r'.\test.png'))
    print(hires_fix(r'.\test.png', r'.\test2.png'))

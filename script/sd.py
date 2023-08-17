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


def figure(path, text):
    '''人物lora和prompt固定'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'

    # 获取figure表中的所有数据
    sql = '''SELECT * FROM figure'''
    data = database.select_data(sql, (), '%stemperature.db' % path)

    prompt = ''
    # 循环检索任务,人名在上的优先
    for i in data:
        # 核对人名
        # 检测i[1],i[2],i[3]是否在text中(排除None数据)
        if (i[1] and i[1] in text) or (i[2] and i[2] in text) or (i[3] and i[3] in text):
            # 如果人名在文本中
            prompt = "%s,%s" % (i[4], i[5])
            break
    return prompt


def sd_text2img(path, main_id):
    '''将main表中的prompt转换为图片的任务加入sd_queue表中'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'
    # 获取main表中的prompt_id和text,并到gpt_queue表中获取completion
    sql = '''SELECT prompt_id,text FROM main WHERE id=?'''
    data = database.select_data(sql, (main_id,), '%stemperature.db' % path)[0]
    prompt_id = data[0]
    text = data[1]
    sql = '''SELECT completion FROM gpt_queue WHERE id=?'''
    completion = database.select_data(
        sql, (prompt_id,), '%stemperature.db' % path)[0][0]

    prompt = ''
    # 人物lora和prompt固定
    text = figure(path, text)
    if text:
        prompt = text+','
    prompt += completion

    # 将main_id,operate,state加入sd_queue表的队列中，并获取该任务的id(id从大到小排序)
    sql = '''INSERT INTO sd_queue(main_id,operate,state) VALUES(?,0,2)'''
    database.change_data(sql, (main_id,), '%stemperature.db' % path)
    # 获取该任务的id(取偏大的id)
    sql = '''SELECT id FROM sd_queue WHERE main_id=? operate=0 state=2 ORDER BY id DESC'''
    id = database.select_data(sql, (main_id,), '%stemperature.db' % path)[0][0]

    # 将main表中的pic_id更新为该id
    sql = '''UPDATE main SET pic_id=? WHERE id=?'''
    database.change_data(sql, (id, main_id), '%stemperature.db' % path)

    return True


def sd_change_pic(path: str, main_id: int):
    '''生成的图片不符合预期标准，重新生成'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'

    # 清除main表的pic_id,hire_fix_id
    sql = '''UPDATE main SET pic_id=NULL,hire_fix_id=NULL WHERE id=?'''
    database.change_data(sql, (main_id,), '%stemperature.db' % path)

    # 重新生成
    sd_text2img(path, main_id)


def change_figure(path: str, data: tuple):
    '''修改人物信息
    data:(name1,name2,name3,lora,prompt,id)'''

    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'
    # 修改figure表中的数据
    sql = '''UPDATE figure SET name1=?,name2=?,name3=?,lora=?,prompt=? WHERE id=?'''
    database.change_data(
        sql, (data[0], data[1], data[2], data[3], data[4], data[5]), '%stemperature.db' % path)
    return True


def get_figure(path: str) -> list:
    '''获取人物信息'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'
    # 获取figure表中的数据
    sql = '''SELECT * FROM figure'''
    data = database.select_data(sql, (), '%stemperature.db' % path)
    return data


def sd_confirm(path, main_id):
    '''确认了main表中的图片符合要求'''
    # 检查path是否加上/
    if path[-1] != '/':
        path += '/'
    # 将main_id,operate,state加入sd_queue表的队列中，并获取该任务的id(id从大到小排序)
    sql = '''INSERT INTO sd_queue(main_id,operate,state) VALUES(?,?,?)'''
    database.change_data(sql, (main_id, 1, 2), '%stemperature.db' % path)
    # 获取该任务的id(取偏大的id)
    sql = '''SELECT id FROM sd_queue WHERE main_id=? operate=1 state=2 ORDER BY id DESC'''
    id = database.select_data(sql, (main_id,), '%stemperature.db' % path)[0][0]
    # 将main表中的hire_fix_id更新为该id
    sql = '''UPDATE main SET sd_id=? WHERE id=?'''
    database.change_data(sql, (id, main_id), '%stemperature.db' % path)

    return True


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
        # 确认operate操作模式
        if data[2] == 0:
            # 如果是0，说明进行text2img操作
            # 从gpt_queue表中获取completion(main表中的prompt_id为gpt_queue表中的id)

            sql = '''SELECT prompt_id FROM main WHERE id=?'''
            prompt_id = database.select_data(
                sql, (data[1],), '%stemperature.db' % path)[0][0]
            sql = '''SELECT completion FROM gpt_queue WHERE id=?'''
            completion = database.select_data(
                sql, (prompt_id,), '%stemperature.db' % path)[0][0]
            # sd操作
            api_rep = text2img(completion, '%spic/%s.png' % (path, data[0]))
            # 将sd生成的文件路径写入sd_queue表,并将其state更新为4(完成),并存入api_rep
            sql2 = '''UPDATE sd_queue SET path=?,state=4,api_rep=? WHERE id=?'''
            database.change_data(
                sql2, ('%spic/%s.png' % (path, data[0]), api_rep, data[0]), '%stemperature.db' % path)
        elif data[2] == 1:
            # 如果是1，说明进行hires_fix操作
            # 获取图片路径
            sql = '''SELECT pic_id FROM main WHERE id=?'''
            pic_id = database.select_data(
                sql, (data[1],), '%stemperature.db' % path)[0][0]
            sql = '''SELECT path FROM pic_queue WHERE id=?'''
            path_1 = database.select_data(
                sql, (pic_id,), '%stemperature.db' % path)[0][0]

            # sd操作
            api_rep = hires_fix(path_1, '%spic/%s.png' % (path, data[0]))

            # 将sd生成的文件路径写入sd_queue表,并将其state更新为4(完成),并存入api_rep
            sql2 = '''UPDATE sd_queue SET path=?,state=4,api_rep=? WHERE id=?'''
            database.change_data(
                sql2, ('%spic/%s.png' % (path, data[0]), api_rep, data[0]), '%stemperature.db' % path)


if __name__ == '__main__':
    print(text2img('masterpiece,4k,(beautiful face),1girl,white background', r'.\test.png'))
    print(hires_fix(r'.\test.png', r'.\test2.png'))

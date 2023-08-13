from script import database
import webuiapi
from PIL import Image


api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)


def text2img(prompt: str, save_path: str, negative_prompt: str = '', seed: int = -1,
             cfg_scale: int = 7, sampler_name: str = 'DPM++ 2S a Karras',
             width: int = 768, height: int = 512, steps: int = 20,
             enable_hr: bool = False, restore_faces: bool = True):
    '''文本转图像'''
    #从数据库setting表中获取sd_prompt,sd_negative_prompt,sd_seed,sd_cfg_scale,sd_sampler_name,sd_width,sd_height,sd_steps,sd_restore_faces
    sql = '''SELECT sd_prompt,sd_negative_prompt,sd_seed,sd_cfg_scale,sd_sampler_name,sd_width,sd_height,sd_steps,sd_restore_faces FROM setting WHERE id=1'''
    data = database.select_data(sql, (), 'data/setting.db')[0]
    try:
        result = api.txt2img(prompt=data[0], negative_prompt=data[1], seed=data[2], cfg_scale=data[3],
                                sampler_name=data[4], width=data[5], height=data[6], steps=data[7], enable_hr=enable_hr, restore_faces=data[8])
        result.image.save(save_path)
    except:
        return False
    return save_path


def hires_fix(path: str, save_path: str):
    '''修复高分辨率图像'''
    #从数据库setting表中获取sd_upscaler_1,,sd_upscaling_resize
    sql = '''SELECT sd_upscaler_1,sd_upscaling_resize FROM setting WHERE id=1'''
    data = database.select_data(sql, (), 'data/setting.db')[0]
    try:
        pic = Image.open(path)
        result = api.extra_single_image(image=pic,
                                 upscaler_1=webuiapi.Upscaler.ESRGAN_4x,
                                 upscaling_resize=1.5)
        result.image.save(save_path)
    except:
        return False
    return save_path
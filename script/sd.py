# from script import database
import webuiapi
api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)


def text2img(prompt: str, save_path: str, negative_prompt: str = '', seed: int = -1,
             cfg_scale: int = 7, sampler_name: str = 'DPM++ 2S a Karras',
             width: int = 768, height: int = 512, steps: int = 20,
             enable_hr: bool = False, restore_faces: bool = True):
    '''文本转图像'''
    try:
        result = api.txt2img(prompt=prompt, negative_prompt=negative_prompt, seed=seed, cfg_scale=cfg_scale,
                             sampler_name=sampler_name, width=width, height=height, steps=steps, enable_hr=enable_hr, restore_faces=restore_faces)
        result.image.save(save_path)
    except:
        return False
    return save_path


# result1 = api.txt2img(prompt="girl with red hair",
#                       negative_prompt="ugly, out of frame",
#                       seed=-1,
#                       cfg_scale=7,
#                       sampler_name='DPM++ 2S a Karras',
#                       width=768,
#                       height=512,
#                       steps=20,
#                       enable_hr=False,
#                       restore_faces=True
#                       )

# # result1 PIL图像
# result1.image.save('test.png')


# print(result1.info)


import PIL
from PIL import Image
pic = Image.open('./test.png')
result3 = api.extra_single_image(image=pic,
                                 upscaler_1=webuiapi.Upscaler.ESRGAN_4x,
                                 upscaling_resize=1.5)
print(result3.image.size)
result3.image.save('./test3.png')
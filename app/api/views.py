
from .app import app, templates
from .schemas import VideoFrame
from .api_manage import get_demo_video_url_dict
from app.manage import get_demo_video_content, get_demo_video_descriptions, \
    open_frame_from_base64
from app.ML_module import LightsRecognator

from fastapi import Request
from fastapi.responses import JSONResponse


@app.get('/')
async def index(request: Request):

    actual_demo_num = 5
    demo_video_descriptions = get_demo_video_descriptions()
    demo_video_url_dict = get_demo_video_url_dict(demo_video_descriptions.keys())
    demo_video_src = get_demo_video_content(actual_demo_num)

    return templates.TemplateResponse('base.html', {'request': request,
                                                    'demo_video_src': demo_video_src,
                                                    'demo_video_descriptions': demo_video_descriptions,
                                                    'actual_demo_num': actual_demo_num,
                                                    'demo_video_url_dict': demo_video_url_dict
                                                   })


@app.get('/get_demo_video/{demo_video_num}')
async def get_demo_video(request: Request, demo_video_num: int):

    demo_video_src = get_demo_video_content(demo_video_num)

    return templates.TemplateResponse('video_sourse.html', {'request': request,
                                                            'demo_video_src': demo_video_src})


@app.post('/analize_frame')
async def analize_frame(frame_data: VideoFrame):
    
    actual_frame = open_frame_from_base64(frame_data.frame_base64)

    recognator = LightsRecognator()
    class_num = recognator.get_class(actual_frame)

    return JSONResponse({
        'class_num': class_num
    })
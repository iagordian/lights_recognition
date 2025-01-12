
from pydantic import parse_obj_as
from typing import List

from ..app import app
from ..schemas import DemoVideo, DemoVideoLst
from app.manage import get_all_demo_video_query, get_demo_video_cnt

def get_all_demo_video_list() -> DemoVideoLst:

    all_video_query = get_all_demo_video_query()
    demo_video_list = parse_obj_as(List[DemoVideo], all_video_query)
    demo_video_list = DemoVideoLst(videos=demo_video_list)
    return demo_video_list

def get_demo_video_url_dict(numbers: List[int]) -> List[str]:

    url_dict = {}
    for num in numbers:
        url_dict[num] = app.url_path_for('get_demo_video', demo_video_num=num)

    return url_dict

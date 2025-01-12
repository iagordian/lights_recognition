
from app.models import DemoVideo
from app.db_operations import db_select

from sqlalchemy.orm import Session
from sqlalchemy import CursorResult
from typing import Dict, Optional, Union


@db_select
def get_demo_video_content(video_num: int, db: Session, as_dict: Optional[bool] = True) -> Union[dict, CursorResult]:

    video_content = db.query(DemoVideo.video_content_mp4, DemoVideo.video_content_webm).filter_by(
        number=video_num
    ).first()

    if video_content:

        if as_dict:
            video_content = {
                'mp4': video_content[0],
                'webm': video_content[1],
            }

    return video_content

@db_select
def get_all_demo_video_query(db: Session) -> CursorResult:

    video_content = db.query(DemoVideo).order_by(DemoVideo.number)
    return video_content

@db_select
def get_demo_video_cnt(db: Session) -> int:
    return db.query(DemoVideo.number).count()
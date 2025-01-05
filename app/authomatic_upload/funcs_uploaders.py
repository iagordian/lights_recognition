
from app.db_operations import db_transaction
from app.models import DemoVideo

from typing import Dict
from sqlalchemy.orm import Session


@db_transaction
def upload_demo_videos(videos_data: Dict[int, str], db: Session):

    for number, content in videos_data.items():

        video = DemoVideo(
            number=number,
            video_content_mp4=content['mp4'],
            video_content_webm=content['webm'],
            context=content['context']
        )
        db.add(video)
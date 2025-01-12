
from app.db_operations import db_select
from app.models import DemoVideo

from sqlalchemy.orm import Session

@db_select
def get_demo_video_descriptions(db: Session):

    return {number: context.lower() for number, context in db.query(DemoVideo.number, DemoVideo.context).order_by(DemoVideo.number)}
        
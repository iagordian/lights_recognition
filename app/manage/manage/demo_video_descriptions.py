
from app.db_operations import db_select
from app.models import DemoVideo

from sqlalchemy.orm import Session

@db_select
def demo_video_descriptions(db: Session):

    for number, context in db.query(DemoVideo.number, DemoVideo.context).order_by(DemoVideo.number):
        yield number, context.lower()
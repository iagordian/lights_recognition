
from app.database import Model

from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from typing import Optional

class DemoVideo(Model):

    __tablename__ = 'demo_videos'

    number: Mapped[int] = mapped_column(Integer, primary_key=True, comment='Номер видео')
    video_content_mp4: Mapped[Optional[str]] = mapped_column(String, comment='Содержимое видео в base64, расширение mp4')
    video_content_webm: Mapped[Optional[str]] = mapped_column(String, comment='Содержимое видео в base64, расширение webm')
    context: Mapped[str] = mapped_column(String, comment='Описание контекста видео')

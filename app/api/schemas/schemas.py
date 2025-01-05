
from pydantic import BaseModel, Field

class VideoFrame(BaseModel):
    frame_base64: str = Field(title='Кадр видео в base64')


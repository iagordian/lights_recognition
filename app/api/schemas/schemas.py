
from pydantic import BaseModel, Field, validator, ConfigDict
from typing import List, Dict

class Scheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class VideoFrame(Scheme):
    frame_base64: str = Field(title='Кадр видео в base64')

class DemoVideo(Scheme):

    number: int = Field(title='Номер видео')
    video_content_mp4: str = Field(title='Содержимое видео в base64, расширение mp4')
    video_content_webm: str = Field(title='Содержимое видео в base64, расширение webm')
    context: str = Field(title='Описание контекста видео')

class DemoVideoLst(Scheme):

    videos: List[DemoVideo] = Field(title='Список демонстрационных видео')

    @validator('videos')
    def sort_videos(cls, videos):
        return sorted(videos, key=lambda v: v.number)
    
    def __iter__(self):
        yield from self.videos
    
    def get_actual_demo_video(self, number) -> Dict[str, str]:

        ind = number - 1
        video = self.videos[ind]

        video_content = {
            'mp4': video.video_content_mp4,
            'webm': video.video_content_webm,
        }

        return video_content
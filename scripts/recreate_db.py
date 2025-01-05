

from app.database import Model, engine
from app.authomatic_upload import Uploader, upload_demo_videos


Model.metadata.drop_all(engine, checkfirst=True)
Model.metadata.create_all(engine)

uploader = Uploader()

uploader.take_files({
    'demo_videos': 'video_demo' 
})

uploader.take_uploaders({
    'demo_videos': upload_demo_videos
})

uploader.start_upload()
uploader.log_errors()
uploader.print_message()

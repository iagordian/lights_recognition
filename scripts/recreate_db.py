

from app.database import Model, engine
from app.authomatic_upload import Uploader, upload_demo_videos
from app.files_navigation import create_dir, join_absolute_path

file_path = 'database/file'
file_path = join_absolute_path(file_path)
create_dir(file_path)

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

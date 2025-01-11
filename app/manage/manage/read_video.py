
import cv2
from cv2 import VideoCapture
import base64
import tempfile
import numpy as np
import torch
from typing import Tuple



def open_video_from_file(file_name: str) -> VideoCapture:
    return VideoCapture(file_name)

def open_frame_from_base64(frame_base64) -> torch.Tensor:
    img = cv2.imdecode(np.frombuffer(base64.b64decode(frame_base64), dtype=np.uint8), cv2.IMREAD_COLOR)
    return img

def open_video_from_base64(base64_string: str) -> VideoCapture:

    decoded_video_bytes = base64.b64decode(base64_string)

    temp_file = tempfile.NamedTemporaryFile()
    temp_file.write(decoded_video_bytes)

    return cv2.VideoCapture(temp_file.name)

def get_video_frame_size_from_base64(base64_string: str) -> Tuple[int]:

    video_capture = open_video_from_base64(base64_string)
    width, height = get_video_frame_size(video_capture)
    return width, height

def get_video_frame_size(video_capture: VideoCapture) -> Tuple[int]:
    return video_capture.get(cv2.CAP_PROP_FRAME_WIDTH), video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)


def frames_iterator(video_capture: VideoCapture):

    while video_capture.isOpened():

        read_ok, frame = video_capture.read()
        if not read_ok:
            break

        yield frame

    video_capture.release()
    return
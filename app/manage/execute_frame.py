
from cv2 import VideoCapture
import cv2
import torch

from .read_video import frames_iterator

def execute_frame(video_capture: VideoCapture, video_shape: float) -> torch.Tensor:

    video_frames_cnt = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    actual_frame_number = int(video_frames_cnt * video_shape)

    video_capture.set(cv2.CAP_PROP_POS_FRAMES, actual_frame_number)

    actual_frame = next(frames_iterator(video_capture))

    return actual_frame
import cv2
import shutil

from pathlib import Path


def get_paths(input_dir, exts=None):
    paths = sorted([x for x in input_dir.glob("**/*")])
    if exts:
        paths = list(filter(lambda x: x.suffix in exts, paths))

    return paths

input_dir = Path(r"D:\★かのい\APEX\Outplayed\Apex Legends")

output_dir = Path(r"output")
output_dir.mkdir(exist_ok=True)

for path in get_paths(input_dir, exts=[".mp4"]):
    cap = cv2.VideoCapture(str(path))
    video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    video_len_sec = video_frame_count / video_fps
    print(video_len_sec)
    cap.release()
    if video_len_sec <= 300:
        shutil.move(str(path), "D:\★かのい\APEX\APEX\ゴミ箱")
    

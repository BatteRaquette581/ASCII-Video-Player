import moviepy
import cv2
import moviepy.editor
import moviepy.video
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--fps", required = True, type = int, help = "Frames per second of the original video, so the stopmotion can match the original video's speed.")
parser.add_argument("--duration", required = True, type = float, help = "Duration of the original video (in seconds).")

args = parser.parse_args()
fps = args.fps
duration = args.duration

n_frame: int = 0
def make_frame(time: float) -> None:
    global n_frame
    frame = cv2.imread(f"screenshots/{str(n_frame)}.png")
    n_frame += 1
    return frame

clip: moviepy.editor.VideoClip = moviepy.editor.VideoClip(make_frame, duration = duration)
clip.fps = fps
clip.write_videofile("output.mp4")

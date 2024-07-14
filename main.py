import cv2
import pynput
import pyautogui
import pyperclip
from numpy import array as np_array
from time import sleep
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--video-path", required = True, type = str, help = "Path to the video file.")
parser.add_argument("--frame-delay", required = True, type = float, help = "Delay between pasting each frame.")
parser.add_argument("--enable-screenshots", action = "store_true", help = "Enables taking screenshots at each frame, and stores them in the screenshots folder.")
parser.add_argument("--screenshot-region-x", type = int, help = "Horizontal coordinate of top-left corner of the screenshot area.")
parser.add_argument("--screenshot-region-y", type = int, help = "Vertical coordinate of top-left corner of the screenshot area.")
parser.add_argument("--screenshot-region-w", type = int, help = "Width of screenshot area.")
parser.add_argument("--screenshot-region-h", type = int, help = "Height of screenshot area.")
args = parser.parse_args()

def convert_to_text(frame: np_array) -> str:
    lines: list[str] = []
    for line in frame:
        line_str: str = ""
        for pixel in line:
            brightness: float = sum(pixel) / 3 / 255
            character_index: str = round(min(len(GRAYSCALE) - 1, len(GRAYSCALE) * (1 - brightness)))
            line_str += GRAYSCALE[character_index] * 2
        lines.append(line_str.rstrip())
    return "\n".join(lines)


capture: cv2.VideoCapture = cv2.VideoCapture(args.video_path)
GRAYSCALE: str = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
REGION: tuple[int, int, int, int] = (args.screenshot_region_x, args.screenshot_region_y, args.screenshot_region_w, args.screenshot_region_h)
quit: bool = False

def on_press(key):
    if key == pynput.keyboard.Key.esc:
        global quit
        quit = True
        exit()

listener = pynput.keyboard.Listener(on_press = on_press)
listener.start()

sleep(10)
for frame_index in range(round(capture.get(cv2.CAP_PROP_FRAME_COUNT))):
    if quit: break
    pyperclip.copy(convert_to_text(capture.read()[1]))
    pyautogui.hotkey("ctrl", "v")
    if args.enable_screenshots: pyautogui.screenshot(f"screenshots/{frame_index}.png", REGION)
    pyautogui.hotkey("ctrl", "a")
    sleep(args.frame_delay)

# ASCII Video Player

A CLI application that can convert video frames into text, paste it (and screenshot it), and compile them into a stop-motion like video.

## Requirements

- A computer (PC only)
- [Python 3+](https://www.python.org/downloads/)
- Needed PIP packages, see in Installation section
- A video to play!

## Installation

### Download

If you haven't already, install [Python 3 here](https://www.python.org/downloads/) - any Python 3 version, if you're unsure about which, just click on the downlad button at the top to download the latest version -.
Click on the "Code" button, and then on "Download ZIP", which would download an archive ZIP file with the scripts in it.

### Installing PIP packages

Install PIP packages with this command in the extracted folder (in the command prompt/terminal):
```
pip install -r requirements.txt
```

Finally, create a directory called "screenshots" (case sensitive) in the extracted folder.

## Usage

To learn how to use the main.py file (script that converts the video into text), execute this command:
```python main.py --help```

To learn how to use the create_video.py file (script that compiles the screenshots into a video), execute this command:
```python create_video.py --help```

from flask import Flask, render_template, Response
from flask_opencv_streamer.streamer import Streamer
import cv2

app = Flask(__name__)

port = 5000
require_login = False
streamer = Streamer(port, require_login)
# Open video device 0
video_capture = cv2.VideoCapture(0)


while True:
    _, frame = video_capture.read()

    streamer.update_frame(frame)

    if not streamer.is_streaming:
        streamer.start_streaming()

    cv2.waitKey(30)
    
if __name__ == '__main__':
    app.run(debug=True)
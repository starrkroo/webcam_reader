from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
import cv2
import threading

from django.views.decorators.csrf import csrf_exempt

import pytesseract


# setup tessaract's engine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame_img(self):
        x = self.video.read()[1]
        return x

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


# object of web-camera
cam = VideoCamera()

# /
def home(request):
    return render(request, 'camera_app/index.html')


# /stored_data -- url to store all ajax-data
@csrf_exempt
def stored_data(request):
    if request.method == 'POST':
        print("[TRANSFORMATION] catching data from frame...")

        # catching text from frame
        video_frame = cam.get_frame_img()
        catched_text = pytesseract.image_to_string(video_frame, lang='rus')

        print(catched_text.strip())

        return redirect('/')
    return render(request, 'camera_app/stored_data.html')


# generate video on /test_stream
def generate_video(request):
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

# yields all required frames
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')# Create your views here.




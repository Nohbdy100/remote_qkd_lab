from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading
import cv2
from .forms import CameraRotate


#Loads the webcam1 feed
@gzip.gzip_page
def webcam1(request):
    try:
        cam = VideoCamera(0)
        return StreamingHttpResponse(gen(cam), content_type = "multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'webcam1.html')

#loads the webcam2 feed
def webcam2(request):
    try:
        cam = VideoCamera(1)
        return StreamingHttpResponse(gen(cam), content_type = "multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'webcam2.html')



#Loads the lab env
def lab(request):
    form = CameraRotate(request.POST)
    # If form is valid redirects to homepage with success message
    if form.is_valid():
        print("Angle changed to ", form.cleaned_data['camera_rotation'])
    #Remains on lab page
    else:
        form = CameraRotate()
    context = {'form': form}
    return render(request, 'lab.html', context)




class VideoCamera(object):
    def __init__(self, camera_index=0):
        self.video = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args= ()).start()
        
    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            

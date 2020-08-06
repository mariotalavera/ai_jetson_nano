import cv2

print(cv2.__version__)

# display window resolution.
# This is windows resolution, not cameras.
dispW=640
dispH=480

# Do we needto flip image? yes
flip=2

# This string is for the rasphberrypi camera on pins.  We do not have such.
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# This is for our USB Cam. Neat.
camSet=('nvarguscamerasrc ! video/x-raw(memory:NVMM),'
            'width=1920, '
            'height=1080,'
            'format=NV12,'
            'framerate=30/1 ! '
            'nvvidconv flip-method='+str(flip)+' ! '
            'video/x-raw, width='+str(dispW)+', height='+str(dispH)+', '
            'format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink')
cam=cv2.VideoCapture(0)

while True:
    ret, frame=cam.read()
    
    # START - This is where the magic happens. We would process images here!
    
    cv2.imshow('usbcam',frame)    
    cv2.moveWindow('usbcam',0,0)

    cv2.imshow('usbcam2',frame)    
    cv2.moveWindow('usbcam2',690,0)

    # Create a gray screen from frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayVideo',gray)
    cv2.moveWindow('grayVideo',0,530)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('hsvVideo',hsv)
    cv2.moveWindow('hsvVideo',690,530)
    
    # END - This is where the magic happens. We would process images here!

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

# xrandr
# doing ssh -X
# v4l2-ctl -d /dev/video0 --list-formats-ext
# v4l2-ctl --list-devices
# lsusb

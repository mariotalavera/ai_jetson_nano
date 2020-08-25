import cv2
import numpy as np

# Setting dims of main window and mirroring image
dispW=640
dispH=480
flip=2

# flag for rectangle being selected
goClick=0

# Defaulting mouse event to -1 (signifying no event)
pntStart=(-1,-1)
pntEnd=(-1,-1)

# On mouse click...
def mouse_click(event, x, y, flags, params):
    # Point clicked

    # Vtodo add roi amd put m its owm little qimdow
    global pntStart
    global pntEnd
    global goClick

    # If left mouse is clicked, 
    if event==cv2.EVENT_LBUTTONDOWN:
        # setting endpoint to startpoint
        pntEnd=(x,y)
        pntStart=(x,y)
        goClick=0
    if event==cv2.EVENT_LBUTTONUP:
        pntEnd=(x,y)
        goClick=1
        print('Rectagle goes from',pntStart,'to',pntEnd,'on event.')
        print('x1 ',pntStart[0], ' y1 ',pntStart[1],'.')
        print('x2 ',pntEnd[0], ' y2 ',pntEnd[1],'.')

# Defining camera window
cv2.namedWindow('usbcam')
# Setting up a callback function on mouse event
cv2.setMouseCallback('usbcam', mouse_click)

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera and mirror video
    ret, frame=cam.read()
    frame=cv2.flip(frame,2)
    roi=frame[0:10,0:10]

    if goClick==1:
        # Drawing rectangle on the screen
        frame=cv2.rectangle(frame,pntStart,pntEnd,(255,0,0),4)

        # format is rows:columns
        # ie - start column(y1):end columny2, start row(x1):end row(x2)
        roi=frame[pntStart[1]:pntEnd[1],pntStart[0]:pntEnd[0]]

        cv2.imshow('roiwindow',roi)
        # cv2.error: /tmp/build_opencv/opencv/modules/highgui/src/window.cpp:331: error: (-215) size.width>0 && size.height>0 in function imshow
        cv2.moveWindow('roiwindow',705,0)

    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    keyEvent=cv2.waitKey(1)
    # Mapping 'q' key to exit program.
    if keyEvent==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

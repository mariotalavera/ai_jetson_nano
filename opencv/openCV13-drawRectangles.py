import cv2
import numpy as np

# Defaulting mouse event to -1 (signifying no event)
# evt=-1
pntStart=(-1,-1)
pntEnd=(-1,-1)

# On mouse click...
def click(event, x, y, flags, params):
    # Point clicked
    global pntStart
    global pntEnd
    # If left mouse is clicked, 
    if event==cv2.EVENT_LBUTTONDOWN:
        pntEnd=(x,y)
        pntStart=(x,y)
        # evt=event
    if event==cv2.EVENT_LBUTTONUP:
        pntEnd=(x,y)
        # evt=event
        print('Rectagle goes from',pntStart,'to',pntEnd,'on event')

# Setting dims of main window and mirroring image
dispW=640
dispH=480
flip=2

# Defining camera window
cv2.namedWindow('usbcam')
# Setting up a callback function on mouse event
cv2.setMouseCallback('usbcam', click)

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera and mirror video
    ret, frame=cam.read()
    frame=cv2.flip(frame,2)

    # Drawing rectangle on the screen
    frame=cv2.rectangle(frame,pntStart,pntEnd,(255,0,0),4)

    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    keyEvent=cv2.waitKey(1)
    # Mapping 'q' key to exit program.
    if keyEvent==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

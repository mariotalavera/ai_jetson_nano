import cv2
import numpy as np

# Defaulting mouse event to -1 (signifying no event)
evt=-1
coord=[]
# New array 
img=np.zeros((250,250,3),np.uint8)

# On mouse click...
def click(event, x, y, flags, params):
    # Point clicked
    global pnt 
    # Event
    global evt
    # If left mouse is clicked, 
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse event was : ', event)
        print(x, ',', y)
        pnt=(x,y)
        coord.append(pnt)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        # y is row, x is column
        blue=frame[y,x,0]
        green=frame[y,x,1]
        red=frame[y,x,2]
        print(blue,green,red)
        colorStr=str(blue)+','+str(green)+','+str(red)
        img[:]=[blue,green,red]
        fnt=cv2.FONT_HERSHEY_PLAIN
        # Opposite colors to selection!
        r=255-int(red)
        g=255-int(green)
        b=255-int(blue)
        tp=(b,g,r)
        cv2.putText(img,colorStr,(10,25),fnt,1,tp,2)
        cv2.imshow('myColor', img)

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
    # Read camera
    ret, frame=cam.read()
   
    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,255,0), -1)
        font=cv2.FONT_HERSHEY_PLAIN
        myStr=str(pnts)
        cv2.putText(frame,myStr,pnts,font,1.5,(255,0,0),2)

    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    keyEvent=cv2.waitKey(1)
    # Mapping 'q' key to exit program.
    if keyEvent==ord('q'):
        break
    # Mapping 'c' key to clean the screen.
    if keyEvent==ord('c'):
        coord=[]

cam.release()
cv2.destroyAllWindows()

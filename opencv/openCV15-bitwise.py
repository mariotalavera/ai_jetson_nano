import cv2
import numpy as np

# Setting dims of main window and mirroring image
dispW=640
dispH=480
flip=2

# New black image (all zeros) number type is unsigned int 
img1=np.zeros((dispH,dispW,1), np.uint8)
# make half of the  immage white
img1[0:460,0:320]=[255]

img2=np.zeros((dispH,dispW,1), np.uint8)
img2[190:290,270:370]=[255]

bitAnd=cv2.bitwise_and(img1,img2)
bitOr=cv2.bitwise_or(img1,img2)
bitXor=cv2.bitwise_xor(img1,img2)

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera
    ret, frame=cam.read()

    cv2.imshow('img1', img1)
    cv2.moveWindow('img1',0,510)

    cv2.imshow('img2', img2)
    cv2.moveWindow('img2',705,0)

    cv2.imshow('bitAnd', bitAnd)
    cv2.moveWindow('bitAnd',705,510)

    cv2.imshow('bitOr', bitOr)
    cv2.moveWindow('bitOr',1340,0)

    cv2.imshow('bitXor', bitXor)
    cv2.moveWindow('bitXor',1340,510)

    # masking frame with any masks above
    frame=cv2.bitwise_and(frame,frame,mask=bitXor)    
    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

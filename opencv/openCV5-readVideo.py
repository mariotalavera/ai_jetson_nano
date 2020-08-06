import cv2

# Setting dims of main window and mirroring image
dispW=640
dispH=480
frameRate=30
flip=2

# USB camera setup
cam=cv2.VideoCapture('toptechtoy/videos/mycam.avi') # read from saved video
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera
    ret, frame=cam.read()
    
    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    # Mapping 'q' key to exit program. Increasing weight makes video play slower...
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
outVid.release()
cv2.destroyAllWindows()

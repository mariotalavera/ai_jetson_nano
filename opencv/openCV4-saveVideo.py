import cv2

# Setting dims of main window and mirroring image
dispW=640
dispH=480
frameRate=30
flip=2

# USB camera setup
cam=cv2.VideoCapture(0) # read from usb cam
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

# To file
outVid=cv2.VideoWriter('toptechtoy/videos/mycam.avi',cv2.VideoWriter_fourcc(*'XVID'),frameRate,(dispW,dispH))

while True:
    # Read camera
    ret, frame=cam.read()
    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    outVid.write(frame)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
outVid.release()
cv2.destroyAllWindows()

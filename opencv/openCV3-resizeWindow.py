import cv2

# Setting dims of main window and mirroring image
dispW=960
dispH=720
flip=2

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera
    ret, frame=cam.read()
    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',690,0)

    # Create a B&W version of camera
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Creating smaller versions of both original and B&W cameras
    frameSmall=cv2.resize(frame,(320,240))
    graySmall=cv2.resize(gray,(320,240))

    # Show smaller cameras in windows and move
    cv2.imshow('BW',graySmall)
    cv2.imshow('nanoSmall',frameSmall)
    cv2.moveWindow('BW',0,265)
    cv2.moveWindow('nanoSmall',0,0)
    
    # More windows!
    cv2.imshow('BW2',graySmall)
    cv2.imshow('nanoSmall2',frameSmall)
    cv2.moveWindow('BW2',370,265)
    cv2.moveWindow('nanoSmall2',370,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


# xrandr
# doing ssh -X
# v4l2-ctl -d /dev/video0 --list-formats-ext
# v4l2-ctl --list-devices
# lsusb

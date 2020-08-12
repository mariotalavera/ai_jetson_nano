import cv2

# Setting dims of main window and mirroring image
dispW=640
dispH=480
flip=2

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera
    ret, frame=cam.read()

    # 1. Create a little window and to 'roi' (Region of interest)
    roi=frame[50:250,200:400].copy() # row then column (y,x) backwards

    # 2. Grab just-created window and create gray version.
    roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    # 3. Create a copy of gray window and maky it color.
    roiGray=cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)

    # 4. Put, now gray, version of window back into original window.
    frame[50:250,200:400]=roiGray

    # Show windows on monitor
    cv2.imshow('usbcam',frame)  # Main window
    cv2.imshow('roi',roi)       # Little windo
    cv2.imshow('gray',roiGray)  # Gray versionof little window

    # Position all windows on monitor
    cv2.moveWindow('usbcam',0,0)
    cv2.moveWindow('roi',705,0)
    cv2.moveWindow('gray',705,255)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

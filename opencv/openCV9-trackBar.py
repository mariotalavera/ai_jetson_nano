import cv2

# Setting dims of main window and mirroring image
dispW=640
dispH=480
flip=2

# box dims
boxW=0.1*dispW
boxH=0.1*dispH

def nothing(x):
    pass

# USB camera setup
cam=cv2.VideoCapture(0)
cv2.namedWindow('usbCam')

# Create trackabars
cv2.createTrackbar('xVal','usbCam',10,dispW,nothing)
cv2.createTrackbar('yVal','usbCam',10,dispH,nothing)
cv2.createTrackbar('width','usbCam',10,dispW,nothing)
cv2.createTrackbar('height','usbCam',10,dispH,nothing)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera
    ret, frame=cam.read()

    # Read trackbars
    xVal=cv2.getTrackbarPos('xVal','usbCam')
    yVal=cv2.getTrackbarPos('yVal','usbCam')
    boxW=cv2.getTrackbarPos('width','usbCam')
    boxH=cv2.getTrackbarPos('height','usbCam')
  
    cv2.circle(frame,(xVal,yVal),5,(0,0,255),-1)
    cv2.circle(frame,(xVal+boxW,yVal+boxH),5,(0,255,0),-1)
    cv2.rectangle(frame,(xVal,yVal),(xVal+boxW,yVal+boxH),(255,0,0),2)
    # print(xVal,yVal)
    
    # Show camera in window and move
    cv2.imshow('usbCam',frame)
    cv2.moveWindow('usbCam',0,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

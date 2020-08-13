import cv2

# Params
dispW=640
dispH=480
sqrW=int(0.2*dispW)
sqrH=int(0.2*dispH)
xStartPos=0
yStartPos=0
dx=2
dy=2

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    xStartPos=xStartPos+dx
    yStartPos=yStartPos+dy

    xEndPos=xStartPos+sqrW
    yEndPos=yStartPos+sqrH

    if xEndPos>=dispW or xStartPos==0:
        dx=dx*-1
    if yEndPos>=dispH or yStartPos==0:
        dy=dy*-1
    
    xEndPos=xStartPos+sqrW
    yEndPos=yStartPos+sqrH
               
    # Read camera and mirror frame
    ret, frame=cam.read()
    frame=cv2.flip(frame,2)

    # Create little window 
    roi=frame[yStartPos:yEndPos,xStartPos:xEndPos].copy()
   # roi=frame[yStartPos :xStartPos,yEndPos:xEndPos].copy()

    # Make main frame gray
    frameGray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # I DO NOT UNDERSTAND WHAT I AM DOING HERE
    frameGray=cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)

    # Stick little moving roi into main frame
    frameGray[yStartPos:yEndPos,xStartPos:xEndPos]=roi

    frameGray=cv2.rectangle(frameGray,(xStartPos,yStartPos),(xEndPos,yEndPos),(0,0,255),2)

    # Show camera in window and put in upper left of window
    cv2.imshow('usbcam',frameGray)
    cv2.moveWindow('usbcam',0,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

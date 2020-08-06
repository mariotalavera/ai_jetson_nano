import cv2

# Setting dims of main window and mirroring image
dispW=640
dispH=480

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera
    ret, frame=cam.read()

    # Flip video
    frame=cv2.flip(frame,2)

    # Drawing rectangle on the screen
    frame=cv2.rectangle(frame,(100,100),(140,40),(255,0,0),4)

    # Drawing circle on the screen
    frame=cv2.circle(frame,(320,240),50,(0,0,255),5)

    # Drawing circle on the screen -1 gives solid shape
    frame=cv2.circle(frame,(360,200),20,(0,255,255),-1)

    # Drawing line
    frame=cv2.line(frame,(10,10),(630,470),(0,0,0),3)

    # Drawing arrowed line
    frame=cv2.arrowedLine(frame,(10,470),(630,10),(255,255,255),7)

    # Putting text on video!
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame, 'Mario is here',(100,100),fnt,1,(255,125,190),3)

    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

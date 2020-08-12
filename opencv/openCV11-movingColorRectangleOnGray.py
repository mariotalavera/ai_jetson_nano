import cv2

# Params
dispW=640
dispH=480
sqrW=int(0.2*dispW)
sqrH=int(0.2*dispH)
sqr_x_start=0
sqr_y_start=0
sqr_x_dir='forward'
sqr_y_dir='up'

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # x coords
    if (sqr_x_dir=='forward' and sqr_x_start<=dispW-sqrW):
        sqr_x_start=sqr_x_start+1
    if (sqr_x_dir=='forward' and sqr_x_start==dispW-sqrW):
        sqr_x_dir='backward'
    if (sqr_x_dir=='backward'):
        sqr_x_start=sqr_x_start-1
    if (sqr_x_start==0):
        sqr_x_start=0
        sqr_x_dir='forward'
                
    # y coords
    if (sqr_y_dir=='up' and sqr_y_start<=dispH-sqrH):
        sqr_y_start=sqr_y_start+1
    if (sqr_y_dir=='up' and sqr_y_start==dispH-sqrH):
        sqr_y_dir='down'
    if (sqr_y_dir=='down'):
        sqr_y_start=sqr_y_start-1
    if (sqr_y_start==0):
        sqr_y_start=0
        sqr_y_dir='up'
                
    sql_x_end=sqr_x_start+sqrW
    sql_y_end=sqr_y_start+sqrH

    # Read camera and mirror frame
    ret, frame=cam.read()
    frame=cv2.flip(frame,2)

    # Create little window 
    roi=frame[sqr_y_start:sql_y_end,sqr_x_start:sql_x_end].copy()
   # roi=frame[sqr_y_start:sqr_x_start,sql_y_end:sql_x_end].copy()

    # Make main frame gray
    frameGray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # I DO NOT UNDERSTAND WHAT I AM DOING HERE
    # explainer for this is at lessin 21 11 minute mark. TODO 
    frameGray=cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)

    # Stick little moving roi into main frame
    frameGray[sqr_y_start:sql_y_end,sqr_x_start:sql_x_end]=roi

    frameGray=cv2.rectangle(frameGray,(sqr_x_start,sqr_y_start),(sql_x_end,sql_y_end),(0,0,255),2)


    # Show camera in window and put in upper left of window
    cv2.imshow('usbcam',frameGray)
    cv2.moveWindow('usbcam',0,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

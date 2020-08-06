import cv2

# Setting dims of main window and mirroring image
dispW=640
dispH=480

# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

# Square parameters, starting
sqrW=int(0.1*dispW)
sqrH=int(0.1*dispH)
sqr_x_start=0
sqr_y_start=0
sqr_x_dir='forward'
sqr_y_dir='up'

while True:
    # Read camera
    ret, frame=cam.read()

    # Flip video
    frame=cv2.flip(frame,2)

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

    # print('x coords ',sqr_x_start,sql_x_end)
    # print('y coords ',sqr_y_start,sql_y_end)

    # Drawing rectangle on the screen
    # Five arguments
    # 1. Frame to draw on
    # 2. Upper left point
    # 3. Lower right point
    # 4. RGB color
    # 5. Line thickness
    frame=cv2.rectangle(frame,(sqr_x_start,sqr_y_start),(sql_x_end,sql_y_end),(255,0,0),3)

    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

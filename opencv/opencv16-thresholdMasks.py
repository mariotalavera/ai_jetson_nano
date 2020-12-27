# Lesson 24
import cv2

# Trackbar
def nothing():
    pass

# Creating Trackbar for blending windows
cv2.namedWindow('Blended')
cv2.createTrackbar('BlendValue','Blended',50,100,nothing)

# Setting dims of main window and mirroring image
dispW=320
dispH=240
flip=2

# Load logo image
cvLogo=cv2.imread('toptechtoy/cv.jpg')
cvLogo=cv2.resize(cvLogo,(dispW,dispH))
cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('cv logo gray',cvLogoGray)
cv2.moveWindow('cv logo gray',0,dispH+60)

# Background mask
_,BGMask=cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('Background Mask',BGMask)
cv2.moveWindow('Background Mask',dispW+60,0)

# Foreground mask
FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask',FGMask)
cv2.moveWindow('FG Mask',dispW+60,dispH+60)

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',2*dispW+70,dispH+60)


# USB camera setup
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    # Read camera
    ret, frame=cam.read()
    frame=cv2.flip(frame,2)

    # Background image
    BG=cv2.bitwise_and(frame,frame,mask=BGMask)
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',2*dispW+70,0)

    # Combine images! (Composite image)
    compImage=cv2.add(BG,FG)
    cv2.imshow('compImage',compImage)
    cv2.moveWindow('compImage',3*dispW+70,0)

    BV1=cv2.getTrackbarPos('BlendValue', 'Blended')/100
    BV2=1-BV1

    # Blended Image
    Blended=cv2.addWeighted(frame,BV1,cvLogo,BV2,0)
    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',3*dispW+70,dispH+60)

    # Another FG!!
    FG2=cv2.bitwise_and(Blended,Blended,mask=FGMask)
    cv2.imshow('FG2',FG2)
    cv2.moveWindow('FG2',4*dispW+70,0)

    # Final composition
    compFinal=cv2.add(BG,FG2)
    cv2.imshow('compFinal',compFinal)
    cv2.moveWindow('compFinal',4*dispW+70,dispH+60)

    # Show camera in window and move
    cv2.imshow('usbcam',frame)
    cv2.moveWindow('usbcam',0,0)

    # Mapping 'q' key to exit program.
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


# Has homework!
# Go same place and grab another image... ~1:01 into video

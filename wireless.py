import cv2
import time 
import numpy as np
import handdetection as hd
import math 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]

wcam,hcam=640,480
cam=cv2.VideoCapture(0)
cam.set(3,wcam)
cam.set(4,hcam)
Ptime=0
vol,volBar,volPer=0,400,0

detector=hd.handDetector(detectionCon=0.9,maxHands=1)

while True:
    success,img=cam.read()
    if not success:
            break
    
    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img)
    if len(lmList)!=0:

        area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1]) //100
        if 250< area <1000:
            length,img,lineInfo=detector.findDistance(4,8,img)
            vol=np.interp(length,[50,300],[minVol,maxVol])
            volBar=np.interp(length,[50,300],[400,150])
            volPer=np.interp(length,[50,300],[0,100])
            smoothness=10
            volPer=smoothness * round(volPer/smoothness)

            fingers=detector.fingersUp()
            if not fingers[4]:
                volume.SetMasterVolumeLevel(vol, None)
                cv2.circle(img,(lineInfo[4],lineInfo[5]),12,(0,255,0),cv2.FILLED)


        cv2.rectangle(img,(50,150),(80,400),(0,0,0),3)
        cv2.rectangle(img,(50,int(volBar)),(80,400),(0,0,255),cv2.FILLED)
        cv2.putText(img,f'{int(volPer)}%',(40,450),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
             
    Ctime=time.time()
    fps=1/(Ctime-Ptime)
    Ptime=Ctime
    cv2.putText(img,f'FPS : {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)

    cv2.imshow("Wireless Sound Controller",img)
    if cv2.waitKey(1)==ord('q'):
        break

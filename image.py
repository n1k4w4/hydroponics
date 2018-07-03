import cv2
import numpy as np
from datetime import datetime

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    b = True

    #last_time = datetime.now()
    #interval = 60

    while True:
        ret,frame = cam.read()

        now = datetime.now()
        fntime = lambda n : int(n.strftime('%H'))
       # sec = fntime(now) - fntime(last_time)
        
        
        #if sec < 0:
           # sec = sec * -1
       # print(now, last_time)
        if (fntime(now) % 4 == 0):
            f = now.strftime('%Y-%m-%d-%H-%M-%S') + ".jpg"
            if b:
                cv2.imwrite(f,frame)
                b = False
                print("save={}, bool={}".format(f, b))
           # last_time = now
        else:
            b = True
        
        cv2.imshow("Input",frame)

        key = cv2.waitKey(10)

        if key == 60:
            cv2.destroyAllWindows()
            break

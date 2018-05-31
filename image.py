import cv2
import numpy as np
from datetime import datetime

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)

    last_time = datetime.now()
    interval = 10

    while True:
        ret,frame = cam.read()

        now = datetime.now()
        fntime = lambda n : int(n.strftime('%S'))
        sec = fntime(now) - fntime(last_time)

        if sec < 0:
            sec = sec * -1
        #print(sec)

        if sec > interval:
            f = now.strftime('%Y-%m-%d-%H-%M-%S') + ".jpg"
            cv2.imwrite(f,frame)
            last_time = now
            print("save=",f)
        
        cv2.imshow("Input",frame)

        key = cv2.waitKey(10)

        if key == 27:
            cv2.destroyAllWindows()
            break

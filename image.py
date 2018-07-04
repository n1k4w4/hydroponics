import cv2
import numpy as np
from datetime import datetime

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    b = True

    while True:
        ret,frame = cam.read()

        now = datetime.now()
        fntime = lambda n : int(n.strftime('%H'))
        
        if (fntime(now) % 4 == 0):
            f = now.strftime('%Y-%m-%d-%H-%M-%S') + ".jpg"
            if b:
                cv2.imwrite(f,frame)
                b = False
                print("save={}, bool={}".format(f, b))
        else:
            b = True
        
        cv2.imshow("Input",frame)

        key = cv2.waitKey(10)

        if key == 27:
            cv2.destroyAllWindows()
            break

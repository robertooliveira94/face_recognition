import cv2
from datetime import datetime

# datetime object containing current date and time
# now = datetime.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

c_fora = 0

while(True):
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    c_fora+=1

    if c_fora % 60 == 0:
        print(c_fora)
        print(frame.shape)
        # ret, frame = cap.set(1, c_fora)
        # now = datetime.now()
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # print(frame.shape, " date and time =", dt_string)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Tchupicha', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # frame = frame[:, :, ::-1]
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print(frame.shape, " date and time =", dt_string)
    # print(frame.shape)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

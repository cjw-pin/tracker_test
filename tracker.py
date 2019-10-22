import cv2

tracker = cv2.TrackerBoosting_create()
tracker_name = str(tracker).split()[0][1:]

cap = cv2.VideoCapture('ilya.mp4')
ret, frame = cap.read()
roi = cv2.selectROI(frame, False)
ret = tracker.init(frame, roi)

count = 0
while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)

    (x, y, w, h) = tuple(map(int, roi))

    if success:
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)

    count = count + 1

    cv2.imshow(tracker_name, frame)
    #cv2.imwrite("frame%d.jpg" % count, frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

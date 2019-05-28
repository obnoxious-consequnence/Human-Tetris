import cv2 as cv
import numpy as np
import argparse
import matplotlib.pyplot as plt
import poses

# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='Path to image or video. Skip to capture frames from camera')
# parser.add_argument('--thr', default=0.2, type=float, help='Threshold value for pose parts heat map')
# parser.add_argument('--width', default=368, type=int, help='Resize input to specific width.')
# parser.add_argument('--height', default=368, type=int, help='Resize input to specific height.')

# args = parser.parse_args()

BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Head"] ]

font = cv.FONT_HERSHEY_SIMPLEX
fontColor = (0, 0, 255)

def cam_picture(pose_nr, req_pose):
    cap = cv.VideoCapture(0)
    seconds = 4

    millis = seconds * 1000
    while (millis > 1000):
    # Capture frame-by-frame
        ret, frame = cap.read()
        millis = millis - 10
    # Display the resulting frame
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        
        cv.putText(frame, str(int(millis / 1000)), (int(frameWidth / 2), 20), font, 0.6, fontColor, 1, cv.LINE_AA)
        cv.putText(frame, str(req_pose), (20, 20), font, 0.6, fontColor, 1, cv.LINE_AA)
        cv.imshow('video recording', frame)

        if cv.waitKey(10) & 0xFF == ord('q'):
        # #this method holds execution for 10 milliseconds, which is why we 
        # #reduce millis by 10
            break

    #once the while loop breaks, write img
    img_name = "imgs/0{}_{}.jpg".format(pose_nr + 1, req_pose)
    cv.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    return img_name

def coords_handler(points):
    xs = []
    ys = []
    res = []

    # Removing NoneTypes
    for coords in points:
        if coords != None:
             res.append(coords)

    # Seperating xsand ys from points
    for coords in res:
        xs.append(coords[0])
        ys.append(coords[1])

    return xs, ys

def openpose(image, req_pose):
    inWidth = 368
    inHeight = 368
    thr = 0.2

    net = cv.dnn.readNetFromTensorflow("graph_opt.pb")
    cap = cv.VideoCapture(image)

    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            cv.waitKey()
            break

        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        
        net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
        out = net.forward()
        out = out[:, :14, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 14 elements

        assert(len(BODY_PARTS) == out.shape[1]) # out.shape[1] = 14

        points = []
        for i in range(len(BODY_PARTS)):
            # Slice heatmap of corresponging body's part.
            heatMap = out[0, i, :, :]

            # Originally, we try to find all the local maximums. To simplify a sample
            # we just find a global one. However only a single pose at the same time
            # could be detected this way.
            _, conf, _, point = cv.minMaxLoc(heatMap)
            x = (frameWidth * point[0]) / out.shape[3]
            y = (frameHeight * point[1]) / out.shape[2]
            # Add a point if it's confidence is higher than threshold.
            points.append((int(x), int(y)) if conf > thr else None)

        for pair in POSE_PAIRS:
            partFrom = pair[0]
            partTo = pair[1]
            assert(partFrom in BODY_PARTS)
            assert(partTo in BODY_PARTS)

            idFrom = BODY_PARTS[partFrom]
            idTo = BODY_PARTS[partTo]

            # font = cv.FONT_HERSHEY_SIMPLEX
            # fontColor = (0, 0, 255)

            if points[idFrom] and points[idTo]:
                cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
                
                cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
                cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
        
                cv.putText(frame, str(partTo), points[idTo], font, 0.5, fontColor, 1, cv.LINE_AA)
                cv.putText(frame, str(partFrom), points[idFrom], font, 0.5, fontColor, 1, cv.LINE_AA)

        xs, ys = coords_handler(points)
        res = poses.tpose(ys)

        cv.putText(frame, res, (20,20), font, 0.5, fontColor, 1, cv.LINE_AA)

        img_name = '{}_score.jpg'.format(req_pose)
        cv.imwrite('imgs/'+img_name, frame)

        break
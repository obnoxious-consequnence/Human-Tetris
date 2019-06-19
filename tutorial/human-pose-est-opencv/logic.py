import cv2 as cv
import numpy as np
import argparse
import matplotlib.pyplot as plt
import poses
import os
import time

# Setting up a dict with names corresponding to the point id
BODY_PARTS = {
    "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
    "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
    "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13
}

# Setting up links, bewteen the body points.
POSE_PAIRS = [
    ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
    ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
    ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
    ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Head"]
]

font = cv.FONT_HERSHEY_SIMPLEX
fontColor = (0, 0, 255)


def coords_handler(points):
    xs = []
    ys = []
    res = []

    # Removing NoneTypes
    for coords in points:
        if coords != None:
            res.append(coords)
        else:
            res.append((0, 0))
    # Seperating xsand ys from points
    for coords in res:
        xs.append(coords[0])
        ys.append(coords[1])

    return xs, ys


def openpose(image, req_pose, counter):
    inWidth = 368
    inHeight = 368
    thr = 0.2

    # Selecting our model (Mobilenet_thin)
    # https://github.com/ildoonet/tf-pose-estimation/tree/master/models/graph/mobilenet_thin
    net = cv.dnn.readNetFromTensorflow("graph_opt.pb")
    cap = cv.VideoCapture(image)

    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            cv.waitKey()
            break

        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]

        # Creates 4-dimensional blob from image. Optionally resizes and crops image from center,
        # subtract mean values, scales values by scalefactor, swap Blue and Red channels.
        net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                                          (127.5, 127.5, 127.5), swapRB=True, crop=False))
        out = net.forward()

        # MobileNet output [1, 57, -1, -1], we only need the first 14 elements
        out = out[:, :14, :, :]

        # Check for errors
        assert(len(BODY_PARTS) == out.shape[1])  # out.shape[1] = 14

        points = []
        for i in range(len(BODY_PARTS)):
            # Slice heatmap of corresponging body's part.
            heatMap = out[0, i, :, :]

            # .minMaxLoc() returns: minVal, maxVal, minLoc, maxLoc
            _, conf, _, point = cv.minMaxLoc(heatMap)

            # out.shape[3] and out.shape[2] = 46
            x = (frameWidth * point[0]) / out.shape[3]
            y = (frameHeight * point[1]) / out.shape[2]

            # Add a point if it's confidence is higher than threshold.
            points.append((int(x), int(y)) if conf > thr else None)

        for pair in POSE_PAIRS:
            # Declaring variabels and checking for errors
            partFrom = pair[0]
            partTo = pair[1]
            assert(partFrom in BODY_PARTS)
            assert(partTo in BODY_PARTS)

            idFrom = BODY_PARTS[partFrom]
            idTo = BODY_PARTS[partTo]

            # If some part of a body is detectet
            if points[idFrom] and points[idTo]:
                # Drawing lines, ellipse and text
                cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)

                cv.ellipse(frame, points[idFrom], (3, 3),
                           0, 0, 360, (0, 0, 255), cv.FILLED)
                cv.ellipse(frame, points[idTo], (3, 3),
                           0, 0, 360, (0, 0, 255), cv.FILLED)

                cv.putText(frame, str(partTo),
                           points[idTo], font, 0.5, fontColor, 1, cv.LINE_AA)
                cv.putText(frame, str(partFrom),
                           points[idFrom], font, 0.5, fontColor, 1, cv.LINE_AA)

        # Using coords_handler to seperate xs, ys and make none points into (0,0)
        xs, ys = coords_handler(points)

        if (req_pose == 'T_Pose'):
            res = poses.tpose(ys, xs, counter)
        if (req_pose == 'Y_Pose'):
            res = poses.ypose(ys, xs, counter)
        if (req_pose == 'I_Pose'):
            res = poses.ipose(ys, xs, counter)

        # Displays text
        cv.putText(frame, req_pose, (20, 20), font,
                   0.5, fontColor, 1, cv.LINE_AA)
        cv.putText(frame, res, (20, 50), font, 0.5, fontColor, 1, cv.LINE_AA)
        cv.putText(frame, str(counter()), (20, 80),
                   font, 0.5, fontColor, 1, cv.LINE_AA)

        # Saves image
        img_name = '{}_score.jpg'.format(req_pose)
        cv.imwrite('imgs/'+img_name, frame)

        # Returns the result string
        return res

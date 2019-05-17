import cv2 as cv
def tpose(y):
    if y[2] and y[4] == y[0] or y[2] and y[4] > y[0]*1.1:
        res ="This is a perfect t-pose!"
    else:
        res ="Try again sonnyboy"
    return res

def ypose(pose):
    if pose.y.rhand and pose.y.lefthand > pose.y.neck*1.3:
        return True
    else:
        return False
    
def ipose(xs):
    if xs[2] and xs[4] < xs[0] *1.2:
        return print("Success")
    else:
        return print("Fail")
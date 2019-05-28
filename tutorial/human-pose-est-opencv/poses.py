# y[3] == right elbow
# y[6] == left elbow
# y[1] == neck
def tpose(y,x):
    points =0
    if len(y) <= 5:
        res = 'To Few Points Detectet'
    elif y[3] and y[6] == y[1] or (y[3] and y[6] > y[1]*1.2) and (y[3] and y[6] < y[1]*0.8):
        res = "this is at perfect pse"
        if x[11] - x[8] < 50:
            res = 'This is a perfect t-pose!'
            points = points+100
        else:
            res = "You got the arms but remember your legs!"
            points = points+50
    else:
        res ="Try again sonnyboy"
    return res

def ypose(y,x):
    if len(y) <= 5:
        res = 'To Few Points Detectet'
    elif (y[3] and y[6] < y[1]*0.9) and (y[3] and y[6] > y[1]*0.7):
          res ="This is a perfect y-pose!"
    else:
        res ="Try again sonnyboy"
    return res
    
def ipose(y,x):
    if x[2] and x[4] < x[0] *1.2:
        return print("Success")
    else:
        return print("Fail")
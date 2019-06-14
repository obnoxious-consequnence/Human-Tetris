#3 == right elbow
#6 == left elbow
#1 == neck
#11 ==left knee
#8 == right knee

def tpose(y,x,counter):
    if len(y) <= 5:
        res = 'To Few Points Detectet'
    elif y[3] and y[6] == y[1] or (y[3] and y[6] > y[1]*1.2) and (y[3] and y[6] < y[1]*0.8):
        if y[3] and y[6] == y[1] or (y[3] and y[6] > y[1]*1.1) and (y[3] and y[6] < y[1]*0.9):
            if x[11] - x[8] < 50:
                res = 'This is a perfect t-pose!'
                counter(100)
            else:
                res = "You got the arms perfect but remember your legs!"
                counter(60)
        else:
            if x[11] - x[8] < 50:
                res = 'This is a good t-pose!'
                counter(80)
            else:
                res = "You got the arms but remember your legs!"
                counter(50)
    else:
        res ="Try again sonnyboy"
        print(counter(1))
    return res

def ypose(y,x,counter):
    if len(y) <= 5:
        res = 'To Few Points Detectet'
    elif (y[3] and y[6] < y[1]*0.9) and (y[3] and y[6] > y[1]*0.7):
        counter(100)
        res ="This is a perfect y-pose!"
    else:
        res ="Try again sonnyboy"
    return res
    
def ipose(y,x,counter):
    if len(y) <= 5:
        res = 'To Few Points Detectet'
    elif x[3] > x[0] -65 and x[6]<x[0]+65 and x[0] <x[8]+30:
        res="Straight as an arrow"
        print(counter(100))
    else:
        res="Fail"
    return res
    
def egyptian(y,x,counter):
    if x[3] > x[0] -65 and x[6]<x[0]+65 and x[0] <x[8]+30:
        res="Straight as an arrow"
    else:
        res="Fail"
    return res

def crocodile(y,x,counter):
    if x[3] > x[0] -65 and x[6]<x[0]+65 and x[0] <x[8]+30:
        res="Straight as an arrow"
    else:
        res="Fail"
    return res

def kpose(y,x,counter):
    if x[3] > x[0] -65 and x[6]<x[0]+65 and x[0] <x[8]+30:
        res="Straight as an arrow"
    else:
        res="Fail"
    return res
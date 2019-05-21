def tpose(y):
    if len(y) <= 5:
        res = 'To Few Points Detectet'
    elif y[2] and y[4] == y[0] or y[2] and y[4] > y[0]*1.1:
        res = 'This is a perfect t-pose!'
    else:
        res ="Try again sonnyboy"
    return res

def ypose(y):
    if len(y) <= 5:
        res = 'To Few Points Detectet'
    elif y[2] and y[4] > y[0]*1.3:
          res ="This is a perfect y-pose!"
    else:
        res ="Try again sonnyboy"
    return res
    
def ipose(xs):
    if xs[2] and xs[4] < xs[0] *1.2:
        return print("Success")
    else:
        return print("Fail")
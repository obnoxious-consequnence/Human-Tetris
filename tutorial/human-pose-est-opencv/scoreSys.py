def totalPoints():
    sum = 0
    def add(n):
        nonlocal sum
        sum = sum + n
        return sum
    return add

counter = totalPoints()
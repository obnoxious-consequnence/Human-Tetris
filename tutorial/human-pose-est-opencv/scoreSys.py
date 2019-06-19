def totalPoints():
    # Closure function
    # Keeps the value
    sum = 0

    def add(n=0):
        nonlocal sum
        sum = sum + n
        return sum
    return add


counter = totalPoints()

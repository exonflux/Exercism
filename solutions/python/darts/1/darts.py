

def score(x, y):
    distance = x**2 + y**2

    if distance > 100:
        return 0
    elif distance <= 1:
        return 10
    elif distance <= 25:
        return 5
    elif distance <= 100:
        return 1
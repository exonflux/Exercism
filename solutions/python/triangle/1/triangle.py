def equilateral(sides):
    
    return sides[0] == sides[1] == sides[2] and sides[0] > 0


def isosceles(sides):
    sides.sort()
    return sides[0] + sides[1] >= sides[2] and sides[0] > 0 and (sides[0] == sides[1] or sides[1] == sides[2])



def scalene(sides):
    return (sides[0] + sides[1] + sides[2] > 2 * max(sides)) and sides[0] > 0 and not isosceles(sides)
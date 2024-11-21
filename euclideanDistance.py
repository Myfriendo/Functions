
points = [(a,b), (c,d)]
def 	absoluteNumber(x):
    if x< 0:
        return -x
    return x

def euclideanDistance(points):

    x= absoluteNumber((points[1][0]-points[0][0]))
    y= absoluteNumber((points[1][1]-points[0][1]))

    return ((x*x+(y*y)))
from numpy import dot
from numpy.linalg import norm

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    #raise NotImplementedError()
    return sum(abs(val1-val2) for val1,val2 in zip(x,y))

def jaccard_dist(x, y):
    #raise NotImplementedError()
    intersection = len(list(set(x).intersection(y)))
    union = (len(x)+len(y)) - intersection

    return 1 - (float(intersection) / union)

def cosine_sim(x, y):
    #raise NotImplementedError()
    return dot(x,y)/(norm(x)*norm(y))
# Feel free to add more

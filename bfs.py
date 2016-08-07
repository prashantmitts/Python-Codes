## bfs on the graph

###### graph representation is dict of list that is dictonary of ############
###### nodes and the values of nodes is list of nodes with edge  ############

def exp(l):
    i = 0
    g = {}
    while (i < len(l)):
        g[l[i]] = 0
        i +=1
    return g

def lis(l,k):
    l1 = []
    i = 0
    while (i < len(l)):
        l1 += [(l[i],k)]
        i += 1
    return l1

def bfs(g,s):
    explored = exp(list(g.keys()))
    explored[s] = 1
    layer = []
    layer += [(s,0)]
    s = lis(g[s],1)    ## s represents the queue
    while (s != []):
        k = s[0]
        if (explored[(k)[0]] == 0):
            explored[(k)[0]] = 1
            layer += [k]
            s += lis(g[k[0]],k[1] + 1)
        s = s[1:]
    return layer

g = {1:[2],2:[1,3],3:[2]}
print(bfs(g,1))

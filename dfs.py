## dfs on the graph

###### graph representation is dict of list that is dictonary of ############
###### nodes and the values of nodes is list of nodes with edge  ############

def exp(l):
    l1 = {}
    i = 0
    while (i < len(l)):
        l1[l[i]] = 0
        i += 1
    return l1

def lis(l,k):
    l1 = []
    i = 0
    while (i < len(l)):
        l1 += [(l[i],k)]
        i += 1
    return l1

def dfs(g,s):
    q = []    ##this represents queue
    explored = exp(list(g.keys()))
    explored[s] = 1
    q += lis(g[s],1)
    layers = [(s,0)]
    while (q != []):
        k = q[len(q)-1]
        q = q[:(len(q)-1)]
        if (explored[k[0]] == 0):
            explored[k[0]] = 1
            q += lis(g[k[0]],k[1] + 1)
            layers += [k]
    return layers

g = {1:[2],2:[1,3],3:[2,4],4:[3,5],5:[4]}
print(dfs(g,3))

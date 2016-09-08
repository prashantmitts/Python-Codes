class Tree(object):
    def __init__(self,data,lindex,rindex):
        self.left = None
        self.data = data
        self.right = None
        self.lindex = lindex
        self.rindex = rindex
        
    

def getTree(l,n,i,r):
    if (n == 1):
        return Tree(l[0],i,r)
    else:
        x1 = getTree(l[:n//2],n//2,i,i+n//2)
        x2 = getTree(l[n//2:],n-(n//2),i+n//2,r)
        d = max(x1.data,x2.data)
        x = Tree(d,i,r)
        x.left = x1
        x.right = x2
        return x

            
def printT(x):
    if (x == None):
        return ""
    else:
        s1 = printT(x.left)
        s2= printT(x.right)
        s = str(x.data)
        return (s1 + " " + s + " "+s2)

def change(x,i,r):
    c1,c2 = x.lindex,x.rindex
    if (c2-c1 == 1):
        x.data = 1
        return x
    else:
        c = x.left.rindex
        if (c > r):
            x1 = op0(x.left,i,r)
            x.left = x1
            x.data = max(x.right.data,x.left.data)
        elif(i>=c):
            xx = x.right
            x1 = op0(xx,i,r)
            x.right = x1
            x.data = max(x.right.data,x.left.data)
        else:
            xx1 = x.left
            xx2 = x.right
            x1 = op0(xx1,i,c)
            x2 = op0(xx2,c,r)
            x.left = x1
            x.right = x2
            x.data = max(x.right.data,x.left.data)
        return x

def update(x,i,r):
    c1,c2 = x.lindex,x.rindex
    if (c2-c1 == 1):
        return x.data
    if (c1 == i and c2 == r):
        return x.data
    else:
        c= x.left.rindex
        if (c > r):
            return op1(x.right,i,r)
        elif(i >= c):
            return op1(x.right,i,r)
        else:
            x1 = op1(x.left,i,c)
            x2 = op1(x.right,c,r)
            return max(x1,x2)

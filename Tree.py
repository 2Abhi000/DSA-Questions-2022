import queue
class BTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printtree(root):
    if root == None:
        return
    
    print(root.data,end=':')
    if root.left!=None:
        print("L",root.left.data,end=',')
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printtree(root.left)
    printtree(root.right)
def treeinput():
    rootdata=int(input())
    if rootdata == -1:
        return None
    root=BTree(rootdata)
    leftTree=treeinput()
    rightTree=treeinput()
    root.left=leftTree
    root.right=rightTree
    return root
def nodecount(root):
    if root == None:
        return 0
    lc=nodecount(root.left)
    rc=nodecount(root.right)
    return 1+lc+rc
def largenode(root):
    if root == None:
        return -1
    llarge=largenode(root.left)
    rlarge=largenode(root.right)
    la=max(llarge,rlarge,root.data)
    return la

def leafnode(root):
    if root is None:
        return 0
    if root.left==None and root.right==None:
        return 1
    lnode=leafnode(root.left)
    rnode=leafnode(root.right)
    return lnode+rnode
def depthT(root,k):
    if root == None:
        return
    if k==0:
        print(root.data)
        return
    depthT(root.left,k-1)
    depthT(root.right,k-1)

def customdepthT(root,k,d=0):
    if root == None:
        return
    if k==d:
        print(root.data)
        return
    customdepthT(root.left,d+1)
    customedepthT(root.right,d+1)

def removeleaves(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    root.left=removeleaves(root.left)
    root.right=removeleaves(root.right)
    return root
def height(root):
    if root==None:
        return 0
    return 1+max(height(root.left),height(root.right))
'''
o(n2) or o(n log n))
def isBalancedT(root):
    if root ==None:
        return None
    lh=height(root.left)
    rh=height(root.right)
    if lh-rh>1 or rh-lh>1:
        return False
    LiB=isBalancedT(root.left)
    RiB=isBalancedT(root.right)
    if LiB and RiB:
        return True
    else:
        return False
'''
#optmised approach
def isBalancedT(root):
    if root ==None:
        return 0,True
    lh,isLeftBalancedT=isBalancedT(root.left)
    rh,isRightBalancedT=isBalancedT(root.right)
    h=1+max(lh,rh)
    if lh-rh>1 or rh-lh>1:
        return h,False
    if isLeftBalancedT and isRightBalancedT:
        return h,True
    else:
        return h,False
def getisBalanced(root):
    h,isBalanced=isBalancedT(root)
    return isBalanced
#take input using queue
def takeinp():
    q=queue.Queue()
    print("Enter root")
    rootData=int(input())
    if(rootData==-1):
        return None
    root=BTree(rootData)
    q.put(root)
    while(not(q.empty())):
        curr_node=q.get()
        print("Enter the left child of ",curr_node.data)
        leftchildData=int(input())
        if leftchildData !=-1:
            leftchild=BTree(leftchildData)
            curr_node.left=leftchild
            q.put(leftchild)

        print("Enter the right child of ",curr_node.data)
        rightchildData=int(input())
        if rightchildData !=-1:
            rightchild=BTree(rightchildData)
            curr_node.right=leftchild
            q.put(rightchild)
    return root

'''root=treeinput()
printtree(root) 
print(nodecount(root))
print(largenode(root))
print(leafnode(root))
print(depthT(root,2))
#print(customdepthT(root,2))
print(removeleaves(root))
printtree(root)
print(isBalancedT(root))
print(getisBalanced(root))
'''

#_----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#BST
def search(root,x):
    
    if(root==None):
        return None
    elif root.data==x:
        return True
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.right,x)
#search between nodes k1 and k2
def searc(root,k1,k2):
    if(root==None):
        return
    if root.data>k2:
        searc(root.left,k1,k2)
    elif root.data<k1:
        searc(root.right,k1,k2)
    else:
        print(root.data)
        searc(root.left,k1,k2)
        searc(root.right,k1,k2)
#find min element in BST
def minTree(root):
    if root==None:
        return 100000
    leftmin=minTree(root.left)
    rightmin=minTree(root.right)
    return max(leftmin,rightmin,root.data)
#find max element in BST
def maxTree(root):
    if root==None:
        return -100000
    leftmin=maxTree(root.left)
    rightmin=maxTree(root.right)
    return max(leftmin,rightmin,root.data)
#check if tree is BST
def isBST(root):
    if root==None:
        return True
    leftmax=maxTree(root.left)
    rightmin=minTree(root.right)
    if root.data>rightmin or root.data<=leftmax:
        return False
    isLeftBST=isBST(root.left)
    isRightBSt=isBST(root.right)
    return isLeftBST and isRightBSt
#optimised approar for is BST
def isbst(root):
    if root ==None:
        return 10000,-10000,True
    leftmin,leftmaxm,isLeftBST=isbst(root.left)
    rightmin,rightmaxm,isrightBST=isbst(root.right)
    minimum=min(leftmin,rightmin,root.data)
    maximum=max(leftmaxm,rightmaxm,root.data)
    isTreeBST=True
    if root.data<=leftmaxm or root.data>rightmin:
        isTreeBST=False
    if not(isLeftBST) or not(isrightBST):
        isTreeBST=False
    return minimum,maximum,isTreeBST
#isBST efficient approacg
def isbst3(root,minrange,maxrange):
    if root==None:
        return True
    if root.data<minrange or root.data>maxrange:
        return False
    ifleftwithincons=isbst3(root.left,minrange,root.data-1)
    ifrightwithincons=isbst3(root.right,root.data,maxrange)
    return ifleftwithincons and ifrightwithincons
#print path in BST from given node
def nodetoroot(root,s):
    if root==None:
        return None
    if root.data==s:
        l=list()
        l.append(root.data)
        return l
    leftop=nodetoroot(root.left,s)
    if leftop!=None:
        leftop.append(root.data)
        return leftop
    rightop=nodetoroot(root.right,s)
    if rightop!=None:
        rightop.append(root.data)
        return rightop
    else:
        return None
#BST class
class BST:
    def __init__(self):
        self.root=None
        self.numnodes=0
    def isprintTreehelper(self,root):
        if root ==None:
            return
        print(root.data,end=':')
        if root.left!=None:
            print("L",root.left.data,end=',')
        if root.right!=None:
            print("R",root.right.data,end="")
        print()
        self.isprintTreehelper(root.left)
        self.isprintTreehelper(root.right)
    def printTree(self):
        self.isprintTreehelper(self.root)
    def isPresenthelper(self,root,data):
        if root ==None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            return self.isPresenthelper(root.left,data)
        else:
            return self.isPresenthelper(root.right,data)
    def isPresent(self,data):
        return self.isPresenthelper(self.root,data)
    def inshelper(self,root,data):
        if root==None:
            node=BTree(data)
            return node
        if root.data>data:
            root.left=self.inshelper(root.left,data)
            return root
        else:
            root.right=self.inshelper(root.right,data)
            return root
    def insert(self,data):
        self.numnodes+=1
        return self.inshelper(self.root,data)
    def min(self,root):
        if root==None:
            return 10000
        if root.left==None:
            return root.data
        return self.min(root.left)
    def deletehelper(self,root,data):
        if root==None:
            return False,None
        if root.data<data:
            deleted,newrnode=self.deletehelper(root.right,data)
            root.right=newrnode
            return deleted,root
        if root.data>data:
            deleted,newlnode=self.deletehelper(root.left,data)
            root.left=newlnode
            return deleted,root
        if root.left==None and root.right==None:
            return True,None
        if root.left==None:
            return True,root.right
        if root.right==None:
            return True,root.left
        replacement=self.min(root.right)
        root.data=replacement
        deleted,newrnode=self.deletehelper(root.right,replacement)
        root.right=newrnode
        return True,root
            
    def deletedata(self,data):
        deleted,newroot=self.deletehelper(self.root,data)
        if deleted:
            self.numnodes-=1
        self.root==newroot
        return deleted
    def count(self):
        return self.numnodes







#_----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Generic trees- A tree which can have as many as childern possible
class Gtree:
    def __init__(self,data):
        self.data=data
        self.childern=list()
def printGt(root):
    if root==None:
        return
    print(root.data,":" ,end="")
    for child in root.childern:
        print(child.data, ",",end="")
    for child in root.childern:
        printGt(child)
def takeGtinp():
    print("Enter root data")
    rootdata=int(input())
    if rootdata==-1:
        return
    root=Gtree(rootdata)
    print("Enter number of children for ",rootdata)
    childcount=int(input())
    for i in range(childcount):
        child=takeGtinp()
        root.childern.append(child)
    return root
def numnodegt(root):
    if root==None:
        return 0
    c=1
    for child in root.childern:
        c=c+numnodegt(child)
    return c
root=takeinp()
printtree(root)

print(search(root,5))
searc(root,4,3)
minTree(root)
maxTree(root)
isBST(root)
isbst(root)
isbst3(root,-100000,100000)
nodetoroot(root,6)
b=BST()
b.insert(10)
b.insert(5)
print(b.isPresent(10))
print(b.deletedata(10))
print(b.count)
b.printTree()
n1=Gtree(5)
n2=Gtree(6)
n1.childern.append(n2)
printGt(n1)
rooot=takeGtinp()
printGt(rooot)
print(numnodegt(rooot))

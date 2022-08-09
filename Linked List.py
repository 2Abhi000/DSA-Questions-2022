class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
tc= n2
def reversll(head):
    if head is None or head.next is None:
        return head
    sh=reversll(head.next)
    cu=sh
    while cu.next is not None:
        cu=cu.next
    cu.next=head
    head.next=None
    return sh
'''

'''
#optmised approach o(n)
def reversll(head):
    if head is None or head.next is None:
        return head,head
    sh,st=reversll(head.next)
    st.next=head
    head.next=None
    return sh,head
'''
def printinode(head,node):
    c=0
    while(head is not None):
        c=c+1
        head=head.next
        if(c==node):
            print(head.data)
            break
    return
    
def insnode(head,i,data): 
    if i<0:
        return head
    
    if i==0:
        n1=Node(data)
        n1.next=head
        return n1
    
    if head is None:
        return None
    
    sh=insnode(head.next,i-1,data)
    head.next=sh
    return head
        
def printLL(head):
    while(head is not None):
        print(str(head.data) + "->",end='')
        head=head.next
    print("None")
    return
#optmised aproach time colplexity=n 
def takeinp():
    inputt=[int(ele) for ele in input().split()]
    head=None
    tail=None
    for currdata in inputt:
        if currdata == -1:
            break

        newNode=Node(currdata)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
'''
naive approach to take input
Time complexity= n2
def takeinp():
    inputt=[int(ele) for ele in input().split()]
    head=None
    for currdata in inputt:
        if currdata == -1:
            break

        newNode=Node(currdata)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head
'''
#efficient approach O(1)
def reversll(head):
    if head is None or head.next is None:
        return head
    sh=reversll(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return sh
def midpoint(head):
    slow=head
    fast=head
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    print(slow.data)
head=takeinp()
printLL(head)
#insnode(head,2,6)
printLL(head)
#insnode(head,1,9)
printLL(head)
#insnode(head,6,10)
printLL(head)
#printinode(head,0)
head=reversll(head)
printLL(head)
midpoint(head)

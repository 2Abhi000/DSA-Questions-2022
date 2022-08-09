#priority queue
class pqnode:
    def __init__(self,value,p):
        self.value=value
        self.p=p
class pq:
    def __init__(self):
        self.pqq=[]
    def getsize(self):
        return len(self.pqq)
    def isempty(self):
        return self.getsize()==0
    def getmin(self):
        if self.isempty() is True:
            return None
        return self.pqq[0].value
    def __moveup(self):
        childindx=self.getsize()-1
        while childindx>0:
            parentindex=(childindx-1)//2
            if self.pqq[childindx].p<self.pqq[parentindex].p:
                self.pqq[childindx],self.pqq[parentindex]=self.pqq[parentindex],self.pqq[childindx]
                childindx=parentindex
            else:
                break
    def insert(self,value,p):
        pnode=pqnode(value,p)
        self.pqq.append(pnode)
        self.__moveup()
    def __movedown(self):
        parindex=0
        lcindex=2*parindex+1
        rcindex=2*parindex+2
        while lcindex<self.getsize():
            mindex=parindex
            if self.pqq[mindex].p>self.pqq[lcindex].p:
                mindex=lcindex
            if rcindex <self.getsize() and self.pqq[mindex].p>self.pqq[rcindex].p:
                mindex=rcindex
            if mindex==parindex:
                break
            self.pqq[parindex],self.pqq[mindex]=self.pqq[mindex],self.pqq[parindex]
            parindex=mindex
            lcindex=2*parindex+1
            rcindex=2*parindex+2
    def removemin(self):
        if self.isempty():
            return None
        ele=self.pqq[0].value
        self.pqq[0]=self.pqq[self.getsize()-1]
        self.pqq.pop()
        self.__movedown()
        return ele

pq=pq()
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)
for i in range(4):
    print(pq.removemin())

#2d array
#method 1
s=input().split()
n,m=int(s[0]),int(s[1])
l=[[int(j) for j in input().split()] for i in range(n)]
print(l)
#method 2
n=int(input())
li=[[int(j) for j in input().split()] for i in range(n)]
print(li)
#method 3
s=input().split()
n,m=int(s[0]),int(s[1])
b=input().split()
lis=[[int(b[m*i+j]) for j in range(m)] for i in range(n)]
print(lis)
#mthod 4
sr=input().split()
n,m=int(sr[0]),int(sr[1])
bl=sr[2:]
lios=[[int(bl[m*i+j]) for j in range(m)] for i in range(n)]
print(lios)
#print 2d array
for i in range(n):
    for j in range(m):
        print(lios[i][j],end=' ')
    print()
#print 2d jagged array
for row in li:
    for ele in row:
        print(ele,end=' ')
    print()
#print maximum sum in column
def larcolsum(lp):
    n=len(lp)
    m=len(lp[0])
    maxsum=-1
    maxcolindex=-1
    for j in range(m):
        summ=0
        for i in range(n):
            summ+=lp[i][j]
        if summ>maxsum:
            maxcolindex=j
            maxsum=summ
    return maxsum,maxcolindex
lp=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
larsum,larcolindex=larcolsum(lp)
print(larsum,larcolindex)
#print maximum sum in row
def larcolsum(lp):
    n=len(lp)
    m=len(lp[0])
    maxsum=-1
    maxcolindex=-1
    for j in range(m):
        summ=0
        for ele in lp:
            summ+=ele[j]
        if summ>maxsum:
            maxcolindex=j
            maxsum=summ
    return maxsum,maxcolindex
lp=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
larsum,larcolindex=larcolsum(lp)
print(larsum,larcolindex)

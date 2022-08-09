#TOH using recursion
def toh(n,rod1,rod2,rod3):
    if(n==1):
        print("Moved 1st disk from",rod1,"to",rod3)
        return
    toh(n-1,rod1,rod3,rod2)
    print("Moved",n, "disk from",rod1,"to",rod3)
    toh(n-1,rod2,rod1,rod3)
x=toh(5,"a","b","c")

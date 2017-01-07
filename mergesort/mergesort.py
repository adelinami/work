
def merge_sort(a,b,n,m):
    """
    Creates a new ordonated succesion with all elements from two given ordonated series
    
    Args:
        a: the first succesion
        b: the second succesion
        n: the number of elements in a
        m: the number of elements in b
    Returns:
        c: the created succesion using merge sort
    """

    c=[]
    i=0
    j=0
    while i<n and j<m :
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
                
        else:
            c.append(b[j])
            j+=1
                          
    if i<n:
        for l in range(i,n):
                c.append(a[l])
    else:
        for l in range(j,m):
            c.append(b[l])
    return c

if __name__ == "__main__":
    a=[]
    b=[]
    n=int(input("number of elements in a -first succesion :"))
    for i in range (n):
        x=int(input("add number to a"))
        a.append(x)
    m=int(input("number of elements in b -second succesion :"))
    for i in range (m):
        x=int(input("add number to b"))
        b.append(x)
         
    c=merge_sort(a,b,n,m)
    print(c)
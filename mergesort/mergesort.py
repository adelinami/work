
__all__ = ["merge_sort"]

def merge_sort(a,b): 
    """
    Creates a new sorted succesion with all elements from two given sorted series
    
    Args:
        a: the first succesion
        b: the second succesion
    Returns:
        c: the created succesion using merge sort
    """

    c=[]
    i=0
    j=0
    a_size=len(a)
    b_size=len(b)
    if a_size==0: 
        return b
    if b_size==0:
        return a
    
    while i<a_size and j<b_size :
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
                
        else:
            c.append(b[j])
            j+=1
                          
    if i<a_size:
        for l in range(i,a_size):
                c.append(a[l])
    else:
        for l in range(j,b_size):
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
         
    c=merge_sort(a,b)
    print(c)

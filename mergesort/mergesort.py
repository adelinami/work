
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
    
    if len(a)==len(b)==0:
        return c
    if len(a)==0: 
        return b
    if len(b)==0:
        return a
    
    while i<len(a) and j<len(b) :
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
                
        else:
            c.append(b[j])
            j+=1
                          
    if i<len(a):
        for l in range(i,len(a)):
                c.append(a[l])
    else:
        for l in range(j,len(b)):
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

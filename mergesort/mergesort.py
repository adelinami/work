
__all__ = ["merge_sort_13"]

def merge_sort_13(a,b):
    """
    Creates a new sorted succesion with all elements from two given sorted series
    
    Args:
        a: the first succesion
        b: the second succesion
    Returns:
        new_list: the created succesion using merge sort
    """

    new_list=[]
    pos_a=0 #index for a
    pos_b=0 #index for b

    if len(a)==0:
        return b
    if len(b)==0:
        return a
    if len(a)==len(b)==0:
        return new_list
    while pos_a<len(a) and pos_b<len(b) :
        if a[pos_a]<b[pos_b]:
            new_list.append(a[ pos_a])
            pos_a+=1
                
        else:
            new_list.append(b[pos_b])
            pos_b+=1
                          
    if pos_a<len(a): #if one of the lists is longer than the other
        for l in range(pos_a,len(a)):
                new_list.append(a[l])
    else:
        for l in range(pos_b,len(b)):
            new_list.append(b[l])
    return new_list

if __name__ == "__main__":
    new_list=[]
    tuple = [1,2], [1,2,3], [1,3,5], [1,6,8], [3,9], [3,4,8], [0], [], [9], [10], [11], [12], [13]
    for position in range( 13):
        new_list=merge_sort_13(new_list,tuple[position])
    print(new_list)
    

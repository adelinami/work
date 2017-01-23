
__all__ = ["merge_sort"]


# Note how this function is 'private' and not exported - its 'internal', not part of the API
def _merge_sort_2(a,b):
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


def merge_sort(o_lists):
    """
    Merges sorted lists.

    Args:
        o_lists: a list of sorted lists
    Returns:
        an ordered list containing the elements of the lists passed in
    """

    res = list()
    for l in o_lists:
        res = _merge_sort_2(res, l)

    return res


if __name__ == "__main__":
    l = [[1,2,3], [2,5,6], [4,7,9]]

    print(merge_sort(l))


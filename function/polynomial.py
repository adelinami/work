'''
Created on Dec 26, 2016

@author: Adelina
'''
import math
def read():
    """
    reads values for a b c
    """
    a=int(input("value for a:"))
    b=int(input("value for b:"))
    c=int(input("value for c:"))
    print(function(a,b,c))
    
def function(a,b,c):
    """
    resolves a quadratic ecuation
    """
    delta=0
    if a==0:
        print("not a quadratic ecuation")
    else:
        delta=b*b-4*(a*c)
        if delta>=0:
            x1=(b*(-1)+math.sqrt(delta))/(2*a)
            x2=(b*(-1)-math.sqrt(delta))/(2*a)
            return(x1,x2)
        else:
            print("there are no real solutions")

def test_function():
    a=1
    b=4
    c=1
    assert function(a,b,c)==(-0.2679491924311228,-3.732050807568877)
test_function()
read()

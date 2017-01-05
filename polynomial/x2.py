'''
Created on Dec 26, 2016

@author: Adelina
'''
# FIXME:  above is redundant info, provided accurately by the version control system (git) - delete it!


import math
# FIXME: if you need only the 'sqrt' function from this package, import only that - not the whole module


def read(): # FIXME: this name is WAY too generic
    """
    reads values for a b c
    """
    a=int(input("value for a:")) 
    b=int(input("value for b:")) # FIXME: I never said the parameters are integers; what happens if I pass in -for example- a string, or a decimal (this should work)
    c=int(input("value for c:"))
    print(function(a,b,c)) # FIXME: not only reads, but also converts, calculates and prints; limit a function to do only one thing
    # FIXME: it should return the values read, not None 
    
def function(a,b,c): # FIXME: WAY too generic name; a better one would be 'solve_x2'
    """
    resolves a quadratic ecuation 
    """
    # FIXME: say what the parameters are and assumptions (eg. they're numbers), also: when it raises an exception etc.; ALL of these situations should be reflected in tests

    delta=0
    if a==0:
        print("not a quadratic ecuation") # FIXME: better raise an exception - to avoid a polymorphic return type
    else:
        delta=b*b-4*(a*c)
        if delta>=0:
            x1=(b*(-1)+math.sqrt(delta))/(2*a) # FIXME: DRY - https://en.wikipedia.org/wiki/Don't_repeat_yourself 
            x2=(b*(-1)-math.sqrt(delta))/(2*a)
            return(x1,x2) # FIXME: (x1, x2,) see http://stackoverflow.com/questions/7992559/python-tuple-trailing-comma-syntax-rule
        else:
            print("there are no real solutions")

    # FIXME: ..and should not print, but rather raise an exception, otherwise you have a polymorphic return value (eg. None and x1, x2)

def test_function(): # FIXME: this should move to it's own file, see ..tests/test_polynomial.py
    a=1
    b=4
    c=1
    assert function(a,b,c)==(-0.2679491924311228,-3.732050807568877) # FIXME: trailing comma


# FIXME: any direct user interaction with this file should reside in an 'if __name__ ...' see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
test_function()
read()


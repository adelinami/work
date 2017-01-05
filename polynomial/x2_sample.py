from math import sqrt



__all__ = ["solve_x2", "NoRealSolutionException", "NotQuadraticEqException"]



class NoRealSolutionException(Exception):
    pass


class NotQuadraticEqException(Exception):
    pass


def solve_x2(a, b=0.0, c=0.0):
    """Solves a quadratic equation, being limited to real solutions.

    Args:
        a: the coefficent for x^2, numeric
        b: the coefficent for x^1, numeric
        c: the coefficent for x^0, numeric

    Returns:
        A tuple containing the two real solutions (x1, x2,) - if any

    Raises:
        NotQuadraticEqException if the coefficent for x^2 is zero
        NoRealSolutionException if there are no real solutions to the equation
    """

    if a==0:
        raise NotQuadraticEqException()

    delta = b^2 - 4*a*c

    if delta < 0:
        raise NoRealSolutionException()

    delta_sqrt = sqrt(delta)
    double_a = a*2

    x1 = (-b + delta_sqrt) / double_a
    x2 = (-b - delta_sqrt) / double_a

    return (x1, x2,)


if __name__=='__main__':

    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))

    (x1, x2,) = solve_x2(a, b, c)
    print((x1, x2,))


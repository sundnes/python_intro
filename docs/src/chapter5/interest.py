from math import log as ln

def present_amount(P, r, n):
    return P*(1 + r/100)**n

def initial_amount(A, r, n):
    return A*(1 + r/100)**(-n)

def years(P, A, r):
    return ln(A/P)/ln(1 + r/100)

def annual_rate(P, A, n):
    return 100*((A/P)**(1.0/n) - 1)

def test_all_functions():
    # Define compatible values
    A = 2.31525; P = 2.0; r = 5.0; n = 3
    # Given three of these, compute the remaining one
    # and compare with the correct value (in parenthesis)
    A_computed = present_amount(P, r, n)
    P_computed = initial_amount(A, r, n)
    n_computed = years(P, A, r)
    r_computed = annual_rate(P, A, n)
    def float_eq(a, b, tolerance=1E-12):
        """Return True if a == b within the tolerance."""
        return abs(a - b) < tolerance

    success = float_eq(A_computed,  A)  and \
              float_eq(P_computed, P) and \
              float_eq(r_computed,  r)  and \
              float_eq(n_computed,  n)
    assert success  # could add message here if desired

if __name__ == '__main__':
    test_all_functions()

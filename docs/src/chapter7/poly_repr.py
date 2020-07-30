"""
The three functions here do exactly the same thing, but
use slightly different datastructures and implementation.
"""

def eval_poly_dict(poly, x):
    """
    Thhe argument poly is here a dict containing
    the non-zero polynomial coefficients.
    """
    sum = 0.0
    for power in poly:
        sum += poly[power]*x**power
    return sum

def eval_poly_list(poly, x):
    """
    poly is here a list containing all coefficients
    """
    sum = 0
    for power in range(len(poly)):
        sum += poly[power]*x**power
    return sum

def eval_poly_list_enum(poly, x):
    """
    same as above, but uses the convenient enum
    function to traverse the list.
    """
    sum = 0
    for power, coeff in enumerate(poly):
        sum += coeff*x**power
    return sum

#the same polynomial represented as list and dict:
p_dict = {0: -1, 2: 1, 7: 3}
p_list = [-1, 0, 1, 0, 0, 0, 0, 3]

#evaluate polynomial for x = 2.5
x = 2.5
print(f'For x={x}:')
print(f'eval_poly_dict gives {eval_poly_dict(p_dict,x):g}')
print(f'eval_poly_list gives {eval_poly_list(p_list,x):g}')
print(f'eval_poly_list_enum gives {eval_poly_list_enum(p_list,x):g}')

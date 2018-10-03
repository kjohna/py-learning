"""
take a list of numbers, a, return a list whose elements correspond to the product of all elements of the input list EXCEPT itself, no division allowed.
with division would be:

prod = 1
output = []
for num in a:
    prod *= num
for num in a:
    output.append(prod / num)
print "out chk: " + str(output)

this version uses one for loop, simultaneously constructing left and right parts. see "prod_no_div_2.py" for separate for loops
"""
def prod_no_div(a):
    left_prod = [1] * len(a)
    left_ptmp = 1
    right_prod = [1] * len(a)
    right_ptmp = 1

    #print "left_prod: " + str(left_prod)
    #print "right_prod: " + str(right_prod)

    for i in range(1, len(a)):
        #print "i: " + str(i)
        left_ptmp *= a[i - 1]
        left_prod[i] = left_ptmp
        right_ptmp *= a[len(a) - i]
        right_prod[len(a) - i - 1] = right_ptmp
        #print "left_prod: " + str(left_prod)
        #print "right_prod: " + str(right_prod)
    out = [1] * len(a)
    for i in range(0, len(a)):
        out[i] = left_prod[i] * right_prod[i]
    print "out: " + str(out)

def prod_with_div(a):
    prod = 1
    output = []
    for num in a:
        prod *= num
    for num in a:
        output.append(prod / num)
    print "out chk: " + str(output)

prod_no_div([2,3,6,1,4])
prod_with_div([2,3,6,1,4])

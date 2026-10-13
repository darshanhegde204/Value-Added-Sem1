#GCD of Two Numbers
def gcdOfTwoNumbers(n1, n2):
    # Write your code here
    for i in range (n1,0,-1):
        if n1%i==0 and n2%i==0:
            return i
#Find Divisors of a Number
def findDivisors(n):
    # Write your code here
    arr=[1]
    for i in range (2,(n//2)+1):
        if n%i==0:
            arr.append(i)
    arr.append(n)
    return arr
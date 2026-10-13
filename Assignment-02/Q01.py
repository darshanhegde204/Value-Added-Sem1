#Check for Perfect Number
def isPerfectNumber(n):
    # Write your code here
    sum=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            sum+=i
            if i !=n//i:
                sum+=n//i
    return sum==n
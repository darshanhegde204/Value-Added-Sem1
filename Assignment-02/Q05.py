#Lowest Common Multiple (LCM) of Two Numbers
def findLcm(n1, n2):
    # Write your code here
    gcp=0
    for i in range (n1,0,-1):
        if n1%i==0 and n2%i==0:
            gcp=i
            break
    return n1*n2//gcp
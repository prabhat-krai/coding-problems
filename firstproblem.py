"""
This program finds if a pair of numbers that equal to a user inputted number

"""
a=[1,2,7,2,6,2,6,8,5,3,2,6,8,9,89]
k=14
a=sorted(a)
l=0
r=len(a)-1

while(l<r):
    if(a[l]+a[r]==k):
        print("True")
        break
    else: 
        if(a[l]+a[r]<k):
            l+=1
        else: 
            r-=1

if(l==r):
    print("False")



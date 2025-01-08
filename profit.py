s1=int(input("enter the speed of first cycle "))
s2=int(input("enter the speed of second cycle "))

s3=int(input("enter the speed of third cycle "))

sum=s1+s2+s3

average=sum/3

if average>s1 and average>s2 :
    print("the average speed is greater then speed of s1 and s2")

elif average>s2 and average>s3 :
    print("the average speed is greater then speed of s2 and s3")

elif average>s1 and average>s3 : 
    print("the average speed is greater then speed of s1 and s3")

elif average>s1 :
    print("the average speed is greater then speed of s1")

elif average>s2 :
    print("the average speed is greater then speed of s2")

elif average>s3 :
    print("the average speed is greater then speed of s3")

else:
    print("it is not an valid values ")
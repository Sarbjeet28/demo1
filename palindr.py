a=int(input("enter any no.:"))
temp=a
rev=0
while(a>0):
	ld=a%10
	rev=(rev*10)+ld
	a=a//10
if(temp==rev):
    print("The no. is palindrome")
else:
    print("the no. is not palindrome:")

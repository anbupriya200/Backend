#write a code to implement plaindrome for numbers


num=int(input("TO eNTER THE NUMBER :"))
s=0
temp=num
while(num>0):
    r=num%10
    s=s+r
    if num>9 :
        s=s*10
    num=num//10
print ("The value is :",s)
if s==temp :
    print("It is an palindrom number")
else :
    print("It is not an palindrom number")
    
    

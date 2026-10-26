"""
num=int(input("Enter your number :"))
s=0
tem=num
while(num>0):
    r = num%10
    s=s+r
    if num>9:
        s=s*10
    num=num//10
    
print(s)    
if (tem == s ):
    print("palindrom")
else :
    print("not palindrom")
"""

num=int(input("Enter your number  :"))
s=0
b=0
while (num>0):
    r=num%10
    s=s+r
    num=num//10
print(s)
while(s>0):
    r=s%10
    b=b+r
    s=s//10
#print(s)
print(b)
        

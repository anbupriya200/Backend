
word = "Anbupriya"
for lrt in word :
    print(lrt) 


print("vowel")
word = "Anbupriya"
for lrt in word :
    if lrt in ('a','e','i','o','u','A'):
        print(lrt)

 
print ("without vowle")
word = "Anbupriya"
for lrt in word :
    if lrt not in ('a','e','i','o','u','A'):
        print(lrt)

 
print("number print ")

for i in range (10):
    print(i)

     

print("Reverse")        
for i in range (10,0,-1):
    print(i)
 


print("Multiply")        
for i in range (0,20,4):
    print(i)

 
#word = "Anbupriya"
#count=" "
#for lrt in word :
 #   count+=1
  #  print(count)



print("Serise")
#5,10,17,26,37,_____

num=5
step=5
while(num<100):
    print(num, end=",")
    num=num+step
    step=step+2
 

#3,6,12,24,48
#3,6,12
 
num=3
 
while (num<50):
    print (num,end=",")
    num=num*2
 
 
    






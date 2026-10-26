"""1.keep accepting numbers until the user enters 0, then display their sum.

2. Find the largest and smallest numbers among n inputs.

3. Count how many digits in a number are even and how many are odd.  
If you are completed all the assignment, then write the code to implement above requirements """
total=0
while True:
    num =int (input ("Enter the number :"))
    if(num == 0):
        break
    else :
        print(num)
        total=num+total
print(total)











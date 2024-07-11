n=int(input("n="))
oddcount=0
evencount=0
for num in range(1,n+1):
    if num%2==0:
        evencount+=1
    else:
        oddcount+=1
        
print(evencount,oddcount)
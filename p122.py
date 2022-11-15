x=int(input())
i=1
count=0
sum=0
while i<=x:
    if(i%2!=0):
        count=count+1
        sum=sum+i
    i=i+1
average=sum/count
print(sum)
print(average)

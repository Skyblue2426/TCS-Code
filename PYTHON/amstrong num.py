lst=[]
start=int(input())
end=int(input())
for i in range (10,100):
    n=int (len (str(i)))
    x=i
    sum=0
    while(x!=0):
        sum+=(x%10)**n
        x//=10
    if (sum==i) : lst.append(sum)
print(lst)

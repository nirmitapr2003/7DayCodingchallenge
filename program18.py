# 18.Python Program to Find Armstrong Number in an Interval
l=int(input("Enter the lower limit: "))
u=int(input("Enter the upper limit: "))
temp=0
order=0
digit=0
sum=0
for num in range(l, u+1):
  digit=num
  while digit>0:
    temp=int(digit%10)
    order=temp*temp*temp
    sum=sum+order
    digit=int(digit/10)
  if num == sum:
    print(num,"It is an armstrong number")
   
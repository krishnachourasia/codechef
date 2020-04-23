t = int(input())
while(t):
  t = t-1
  n = int(input())
  arr = input().split()
  total = 0
  for i in range(n):
    arr[i] = int(arr[i])
    total = total + arr[i]
  before = total/n
  after = 0
  flag = 0
  for i in range(n):
    temp = total
    temp = temp - arr[i]
    after = temp/(n-1)
    if(before == after):
      flag = 1
      print(i+1)
      break
  
  if(flag == 0):
    print("Impossible")
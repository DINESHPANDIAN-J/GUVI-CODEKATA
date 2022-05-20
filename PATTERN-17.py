n=int(input())
l=list("*"*n)
for i in range(n,0,-1):
  l[:(i-1)]=" "*(i-1)
  print("".join(l))
  l[:]="*"*n

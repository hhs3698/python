def add(a,b):
    c = a+b 
    print(c)
add(2,3)
#5

def add(a,b):
    c = a+b
    return c

d = add(2,3)
print(d)
#5

def A(a,b):
    c = a+b
    d = a-b 
    return c,d
A(4,2)
#6, 2

a = [3,5,6,4,9]

def isPrime(x):
  for i in range(2, x):
    if x%i == 0:
        return False
  return True

for x in a:
   if isPrime(x):
      print(x, end=" ")
      
# 3 5 

# 1. range()
a = range(10)
print(list(a))
# [0,1,2,3,4,5,6,7,8,9]

# 1-1
a = range(1,10)
 #range(시작값, 끝값)
print(list(a))
# [1,2,3,4,5,6,7,8,9]

#2. for
for i in range(10,0,-2):
    print(i, end=" ")
# 10,8,6,4,2

#3. while 
i = 1
while i<=10:
 print(i, end=" ")
 i+=1
#1,2,3,4,5,6,7,8,9,10
 
#3-2
i = 1
while True:
  if i == 4:
    break
  print(i)
  i+=1

#4. continue
for i in range(1,10):
  if i == 4:
    continue
  print(i, end=" ")
  i+=1

#5. for~else => 연장의 느낌, for 조건을 다 충족하면 마지막 else도 출력함
for i in range(1,6):
    print(i, end=" ")
else:
  print("감사합니다.")
#1,2,3,4,5 감사합니다.

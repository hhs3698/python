# 1. 리스트 만들기
a = list()
b = []
c = [1,2,3,4]
c[0] #1
a = list(range(1,10))
print(a)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 리스트 추가 append, insert
a = [1,2,3]
a.append(4)
print(a) #[1,2,3,4]

a.insert(2,6)
print(a) #[1,2,6,3]

# 3. 리스트 제거 pop,remove
a = [1,2,3]
a.pop() # [1,2]
a.remove(1) #[2,3]

# 4. 리스트 위치 
a = [1,2,3]
print(a.index(1))
#0

# 5. 리스트 정렬,전체 삭제 sort,clear
a = [4,3,2]
a.sort() #[2,3,4]
a.sort(reverse=True) #[4,3,2]
a.clear() #[]

# 6. 
a = [12,43,25,67,98]
for i in range(len(a)):
    print(a[i], end=" ")
# 12,43,25,67,98
for x in a:
    print(x, end=" ")

# 7. 인덱스에 접근하기 enumerate
a = [12,43,25,67,98]
for x in enumerate(a):
  print(x)    
# (0, 12) => 튜플 형태로 나옴
# (1, 43)
# (2, 25)
# (3, 67)
# (4, 98)
  
# 8.
for index, value in enumerate(a):
  print(index, value)
# 0 12
# 1 43
# 2 25
# 3 67
# 4 98  

# 9. 튜플은 값 변경 불가능
  a = (12,43,25,67,98)
  a[2] = 7 #불가능

#10. all, any
if all(60>a for x in a):
   print("yes") #각각의 값이 다 60보다 작으면 yes
else:
   print("no") #하나라도 크면 no 


if any(60>a for x in a):
    print("yes") #하나라도 60보다 작으면 yes
else:
    print("no") #전부 크면 no 


# 1. 값 교환
a = 10 
b = 20
# 갑 교환을 원하는 경우
a,b = b,a 
# 이렇게 작성을 하게 되면 값 교환이 된다.

# 2. sep
a,b = 10,20 
print(a,b, sep="/")
#출력결과 = a/b 

# 3. split()
a,b = input().split()
print(a,b)
# 입력값이 => a b(중간 띄어쓰기 split이 인식) 출력값 a b

# 4. map
a, b = map(int, input().split())
# 출력될 때 바로 int형으로 출력이 됨

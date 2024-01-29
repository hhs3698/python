def plus_one(x):
    return x+1

#람다함수
plus_one = lambda x:x+1
#람다 함수는 항상 변수에 넣어줘야 함 
plus_one(1)

#람다 실 사용 예 
a = [1,2,3]
print(list(map(plus_one,a)))
# [2,3,4]

#람다 함수를 사용하면 함수를 먼저 선언하지 않아도 됨 
a = [1,2,3]
print(list(map(lambda x:x+1, a)))
#[2,3,4]
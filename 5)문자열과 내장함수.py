msg = "It is time"

print(msg.upper())
print(msg.lower())

print(msg.find("T"))
#1
print(msg.count())
#2

print(msg[:2])
#It

print(len(msg))
#9 
for i in range(len(msg)):
    print(msg[i], end=" ")
#It is time
for x in msg:
    print(x, end=" ")
#it is time

x.isupper()
#대문자라면 True
x.islower()


#숫자를 아스키코드로 출력
print(ord("A"))
#65
print(ord("Z"))
#90
print(chr(65))
#A

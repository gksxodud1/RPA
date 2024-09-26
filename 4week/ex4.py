#임의로 정수를 입력 받아서 1~정수까지 합을 구하는 프로그램
#정수합을 구하는 로직은 함수로 만들어야함

def sumfunc(a):
    return



num = int(input("값을 입력하세요."))
sum = 0

for i in range(1, num):
    sum += i
print(f"{sum+num}")

if  num < 1:
    print("1이상의 정수를 입력하시오")



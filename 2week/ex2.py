a=123
b=15.556

print("a:{0} b{1}".format(a, b))
print(f"a:{a} b:{b}")

print(f"a:{a:05d} b:{b:2f}")
print("a:%05d b:%.2f" %(a,b))
print(a,"and",b,sep='@',end='\n\n') ##프린트문은 세퍼레이터나 엔드를 넣을수있음 출력해야할 대상에 대해서 구분을 할수 있고 \n는 줄바꿈 하겠다는 뜻
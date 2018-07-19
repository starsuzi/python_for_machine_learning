#빈칸을 기준으로 문자열 나누기
items = 'zero one two three'.split()
print(items)
#","을 기준으로 문자열 나누기
items1 = 'hello,world,hello,python'.split(',')
print(items1)
#리스트의 각 값을 a,b,c,변수로 unpacking
items2 = 'python,jquery,javascript'
a,b,c = items2.split(",")
print("this is a: "+a)
print("this is b: "+b)
print("this is c: "+c)
#"."을 기준으로 문자열 나누고 unpacking
items3 = 'hello.everyone.bye'
d,e,f = items3.split(".")
print(d)

#test

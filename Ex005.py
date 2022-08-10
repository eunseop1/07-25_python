# 입력받아 출력하기
name = input('이름: ')
# +는 붙어서 나온다
print(name + "씨 방가방가!!")
print(name, "씨 방가방가!!")

#빈칸이 들어간다
print('Hello ', name, '!')
#seq로 빈칸 제거
print('Hello ', name, '!', sep='')
print('Hello ', name, '!', sep='-')
print("{}씨 방가방가!!".format(name))
print("'{0}'씨 방가방가!!".format(name))
print("'{name}'씨 방가방가!!".format(name=name))
print("'{0} {0} {0}'씨 방가방가!!".format(name))
print("'{name}'씨 방가방가!!".format(name=name * 3))

age = input("나이 : ")
print(age, type(age))

age = int(input("나이 : "))
print(age, type(age))
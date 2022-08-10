import sys

print(sys.version)
data = input("Enter a number: ")
print(data, type(data))

data = eval(input("Enter a number: "))
print(data, type(data))

data = int(input("Enter a number(2): "), 2)
print(data, type(data))

data = int(input("Enter a number(8): "), 8)
print(data, type(data))

data = int(input("Enter a number(10): "), 10)
print(data, type(data))

data = int(input("Enter a number(16): "), 16)
print(data, type(data))

# 스트링으로 인식한다
colors = input("Your favourite colours? ")
# Your favourite colours? ["red","green","blue"]
print(colors, type(colors))

# 스스로 판단해서 리스트로 인식한다
colors = eval(input("Your favourite colours? "))
# Your favourite colours? ["red","green","blue"]
print(colors, type(colors))
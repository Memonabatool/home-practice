 # 07 if conditions-------

num = 90
if num ==45:
     print("you are passed")
else:
     print("you are not passed")

num = 100
if (num>=45 and num<=50):
    print("passed")
num = 20
num = 40
if num ==20:
  if num == 40:
    print("you got both right")
else:
   print("you got 2nd wrong")
   print("you got both wrong")

#08 type casting------
num = 45
print(type(num))
num = int(num)
num2 = 45
num2 = str(num2)
print(type(num2))
num3 = 43.8
num3 = float (num3)
print(type(num3))
num4 = 34
num4 = int(num4)
print(type(num4))
num5 = [45]
num5 = list(num5)
print(type(num5))
num6 = ("34")
num6 = set(num6)
print(type(num6))
num7 = {"78"}
num7 = dict(num7)
print(type(num7))
num8 = ("34")
num8 = tuple(num8)
print(type(num8))
value = input("enter you age in number:")
value = int(value)
print(type(value))
num1 = input("enter you name:")
num2 = input("enter you age:")
num1 = str(num1)
num2 = str(num2)
print(type(num1))
print(type(num2))

#09 multiple string----------
a = "hello"
b = " world"
print(a+""+b)
a = 42
b = 34
print(str(a)+str(b))
c = "hello world"
print(str(a)+str(b)+str(c))
d = "hello world""mona"
e = "hallo""AI class"
print(d+" "+e)

#011 format in string and integers/floats-----
marks = 45
total = "your total marks is 100 and you got{}"
obt = total .format(marks)
print(obt) 
age = 24
ab = "your name is mona and your education is matric and you got grade a and your age {}"
print(ab)

#12 slicing method--------
a = "hello world !"
print(a[0:2])
print(a[:3])
print(a[0:])
print(a[:7])
print(a[:5])
 #13 split method in string-------
a = "hello AI class"
b = a.split(",")
print(b)
a = "hello Ai class"
b = a.split(" ")
print(b)
a = "hello,AI,class"
b = a.split(",")
print(b)
a = "heloo class my name is mona and my age is 23"
b = a.split(" ")
print(b)


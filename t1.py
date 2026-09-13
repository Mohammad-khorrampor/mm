# std = {}
# std ["name"]=input("enter name : ")
# print(f"name {std["name"]}")
# std ["age"]=input("enter age : ")
# print(f"age {std["age"]}")
# std ["reshte"]=input("enter reshte : ")
# print(f"reshte {std["reshte"]}")
# std ["city"]=input("city : ")
# print(f"city {std["city"]}")
# std ["uni"]=input("uni : ")
# print(f"uni {std["uni"]}")
# keys=["name","age","reshte","city","uni","score"]
# info={}
# for barare in keys:
#     info[barare]= input(barare+" : ")
#     print(f"{barare}: {info[barare]}")
# if score >= 17 : 
#      print(" eali ")
# elif score >= 14 :
#      print(" khob ")
# elif score >= 10 :
#     print(" gabol ")
# elif score <= 10 :
#     print(" mardod ")
# else:
#     print(" na moetabar ")
# def p(name,age):
#     print(f"name is{name}")
#     print(f"age is{age}")
# std_name=input("enter name")
# std_age=input("enter age")

# p(std_name, std_age)

# def sum_of_nums(x,y):
#     sum=x+y
#     return sum
# num1=int(input(" "))
# num2=int(input(" "))

# res= sum_of_nums(num1,num2)
# print(res)

# def max(a,b):
#     if a>b:
#         return a
#     elif a==b:
#         res="balance"
#         return res
#     else:
#         return b



# a=int(input())
# b=int(input())
# max_of_nums=max(a,b)
# print(f"max of two
# number{a}and{b}is:
# {max_of_nums}")       

# def hello(user="Guest"):
#     print(user)
# # hello()
# hello("shayan")

# def std(name,age):
#     print(name)
#     print(age)
# # std(age=23,name="shayan")
# std("shayan",23)

# def sum_n(num1,num2):
#     sum=num1+num2
#     return sum

# def sub_n(num1,num2):
#     sub=num1-num2
#     return sub

# def mult_n(num1,num2):
#     mult=num1*num2
#     return mult

# def div_n(num1,num2):
#     div=num1/num2
#     return div

# s=sum_n(10,2)
# su=sub_n(10,5)
# m=mult_n(2,6)
# d=div_n(10,2)

# print(f"sum={s} and sub={su} and mult={m} and div={d}")

# def avg_n(num1,num2,num3):
#      sum=num1+num2+num3
#      avg=sum/3
#      return avg
# avg_n(num3=10,num2=10,num1=20)
# avg_n=a
# print(f"avg={a}")

# def mult_n(num1,num2,num3):
#      mult=num1*num2*num3
#      float(mult)=m
#      return m
# mult_n(num3=10,num2=10,num1=20)
# mult_n=a
# print(f"avg={a}")


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "error:tagsim bar 0 momken nist"
#     return  a / b

# print("the four basic operations:")
# print("1.add")
# print("2.sub")
# print("3.mult")
# print("4.div")

# choice = input("select the desired opration(1/2/3/4)")
# num1 = float(input("enter the frist number : ")) 
# num2 = float(input("enter the second number : "))

# if choice == "1":
#     result = add(num1 , num2)
#     print("result:", result)
# elif choice == "2":
#     result = subtract(num1 , num2)
#     print("result:", result)
# elif choice == "3":
#     result = multiply(num1 , num2)
#     print("result:", result)
# elif choice == "4":
#     result = divide(num1 , num2)
#     print("result:", result)
# else:
#     print("invalid opreration")

# import math
# import random
# print(math.sqrt(25))
# print(random.randint(1,10))
# names=["ali","vali","goli"]
# print(random.choice(names))
# import math
# print(math.sqrt(36))
# print(math.pow(2,4))
# print(math.pi)
# calculator.py
# op=str(input("enter op: "))
# num1=float(input("number1:"))
# num2=float(input("number2: "))

# def num_check(a):
#     match a:
#         case 0:
#             return "adad 0 ast"
#         case 1:
#             return "adad 1 ast"
#         case a if a>0:
#             return "adad mosbat ast"
#         case a if a<0:
#             return "adad manfi ast"
#         case _:
#             return "na moshakhase"
# a= int(input("adad vared konid : "))
# res = num_check(a)
# print(res)

# file = open("test.txt","w")
# file.write("hello")
# file.close()
# file = open("test.txt","r")
# print(file.read())
# file.close()
# file = open("test.txt","a")
# file.write("\n shayan")
# file.close()

n = int(input("How many students can you enter? "))
file = open("students.txt","w")
for i in range(n):
    name = input("name : ")
    students_id = ("students id number : ")
    age = input("age : ")
    file.write(f"{name},{students_id},{age}\n")
print("\n saved in the students file . ")
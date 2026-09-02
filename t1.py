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

def max(a,b):
    if a>b:
        return a
    elif a==b:
        res="balance"
        return res
    else:
        return b



a=int(input())
b=int(input())
max_of_nums=max(a,b)
print(f"max of two
number{a}and{b}is:
{max_of_nums}")       
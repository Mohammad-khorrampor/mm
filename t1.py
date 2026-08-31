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
keys=["name","age","reshte","city","uni","score"]
info={}
for barare in keys:
    info[barare]= input(barare+" : ")
    print(f"{barare}: {info[barare]}")
if score >= 17 : 
     print(" eali ")
elif score >= 14 :
     print(" khob ")
elif score >= 10 :
    print(" gabol ")
elif score <= 10 :
    print(" mardod ")
else:
    print(" na moetabar ")
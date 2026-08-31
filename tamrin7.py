keys = ["name", "age", "reshte", "city", "uni", "score"]
info = {}

for md in keys:
    info[md] = input( md + " : ")
    print(f"{md}: {info[md]}")

if float(info["score"]) >= 17:
    print(" eali ")
elif float(info["score"]) >= 14:
    print(" khob ")
elif float(info["score"]) >= 10:
    print(" gabol ")
elif float(info["score"]) < 10:
    print(" mardod ")
else:
    print(" na moetabar")
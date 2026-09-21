FILE_NAME = "students2.txt"
open(FILE_NAME, "a", encoding="utf-8").close()  # اگر فایل نباشد، ساخته شود

while True:
    print("\n--- student menu ---")
    print("1. add std")
    print("2. search std ")
    print("3. display std ")
    print("4. delete std")
    print("5. edit std")
    print("6. exit ")

    choice = input("choose a number : ")

    match choice:
        case "1":
            name = input("name: ")
            age = input("age: ")
            sid = input("std_id: ")
            with open(FILE_NAME, "a", encoding="utf-8") as f:
                f.write(f"{name}|{age}|{sid}\n")
            print("student added.")

        case "2":
            q = input("name or std_id: ")
            found = False
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip() == "":
                        continue
                    name, age, sid = line.strip().split("|")
                    if q == name or q == sid:
                        print(f"name: {name} | age: {age} | id: {sid}")
                        found = True
            if not found:
                print("not found")

        case "3":
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                content = f.read()
                if content.strip() == "":
                    print("the list is empty.")
                else:
                    print(content)

        case "4":
            sid = input("std_id for delete ")
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = f.readlines()
            new_lines = []
            for line in lines:
                if line.strip() == "":
                    continue
                parts = line.strip().split("|")
                if parts[2] != sid:
                    new_lines.append(line)
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print("deletion completed")

        case "5":
            sid = input("std_id for edit:")
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                for line in lines:
                    if line.strip() == "":
                        continue
                    name, age, old_sid = line.strip().split("|")
                    if old_sid == sid:
                        name = input("new name: ")
                        age = input("new age: ")
                        old_sid = input("new id: ")
                    f.write(f"{name}|{age}|{old_sid}\n")
            print("the edit has been made.")

        case "6":
            print("goodbye")
            break

        case _:
            print("please enter the correct number.")
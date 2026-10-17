import json
import os

FILE = "accounts.json"

def load():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return{}
    return {}

def save(accounts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(accounts, f, ensure_ascii=False, indent=2)

def start_acc(accounts):
    name = input("Name: ")
    if name in accounts:
        print("Account already exists.")
        return
    lastname = input("Last name: ")
    pin = input("PIN: ")
    card_id = input("Card ID: ")
    for v in accounts.values():
        if v["card_id"] == card_id:
            print("Card ID already used.")
            return
    accounts[name] = {
        "lastname": lastname,
        "pin": pin,
        "card_id": card_id,
        "balance": 0
    }
    save(accounts)
    print("Account created.")

def login(accounts):
    name = input("Name: ")
    pin = input("PIN: ")
    if name in accounts and accounts[name]["pin"] == pin:
        return name
    print("Wrong name or PIN.")
    return None

def get_amount():
    try:
        amt = float(input("Amount: "))
    except ValueError:
        return None
    if amt <= 0:
        return None
    return amt

def account_menu(accounts, name):
    while True:
        print("1) add\n2) sub\n3) show\n4) transfer\n5) exit")
        ch = input("Choice: ")

        if ch == "1":
            amt = get_amount()
            if amt is None:
                print("Invalid amount."); continue
            accounts[name]["balance"] += amt
            save(accounts)
            print("Done.")

        elif ch == "2":
            amt = get_amount()
            if amt is None:
                print("Invalid amount."); continue
            if amt > accounts[name]["balance"]:
                print("Not enough balance."); continue
            accounts[name]["balance"] -= amt
            save(accounts)
            print("Done.")

        elif ch == "3":
            a = accounts[name]
            print(f"Name: {name} {a['lastname']} | Card: {a['card_id']} | Balance: {a['balance']}")

        elif ch == "4":
            dname = input("Destination name: ")
            dlast = input("Destination last name: ")
            dcard = input("Destination card ID: ")
            dpin = input("Destination PIN: ")

            dest = None
            for k, v in accounts.items():
                if (k == dname and v["lastname"] == dlast
                        and v["card_id"] == dcard and v["pin"] == dpin):
                    dest = k
                    break

            if dest is None:
                print("Destination not found or wrong info."); continue
            if dest == name:
                print("Cannot transfer to yourself."); continue

            amt = get_amount()
            if amt is None:
                print("Invalid amount."); continue
            if amt > accounts[name]["balance"]:
                print("Not enough balance."); continue

            accounts[name]["balance"] -= amt
            accounts[dest]["balance"] += amt
            save(accounts)
            print("Transferred.")

        elif ch == "5":
            return

        else:
            print("Invalid choice.")

def main():
    accounts = load()
    while True:
        print("1) start acc\n2) login acc\n3) exit")
        ch = input("Choice: ")

        if ch == "1":
            start_acc(accounts)
        elif ch == "2":
            user = login(accounts)
            if user is not None:
                account_menu(accounts, user)
        elif ch == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
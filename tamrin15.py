import json
import os

FILE_NAME = "accounts.json"


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """افزایش موجودی"""
        if amount <= 0:
            print("❌ مبلغ واریز باید بیشتر از صفر باشد.")
            return
        self.balance += amount
        print(f"✅ {amount} به حساب {self.name} واریز شد.")

    def withdraw(self, amount):
        """کاهش موجودی"""
        if amount <= 0:
            print("❌ مبلغ برداشت باید بیشتر از صفر باشد.")
            return
        if amount > self.balance:
            print("❌ موجودی کافی نیست!")
            return
        self.balance -= amount
        print(f"✅ {amount} از حساب {self.name} برداشت شد.")

    def show_balance(self):
        """نمایش موجودی"""
        print(f"👤 نام: {self.name} | 💰 موجودی: {self.balance}")

    def to_dict(self):
        return {"name": self.name, "balance": self.balance}


# ---------- توابع کار با فایل ----------

def load_accounts():
    """خواندن اطلاعات از فایل"""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_accounts(accounts):
    """ذخیره اطلاعات در فایل"""
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        json.dump(accounts, f, ensure_ascii=False, indent=4)


# ---------- منوی اصلی ----------

def main():
    accounts_data = load_accounts()


    if accounts_data:
        acc = BankAccount(accounts_data[0]["name"], accounts_data[0]["balance"])
    else:
        name = input(" Enter account holder name:  ")
        acc = BankAccount(name)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. SHow Balance")
        print("4. Save to file")
        print("5. Exit")

        choice = input("Choose an option : ")

        if choice == "1":
            amount = float(input("Deposit amount : "))
            acc.deposit(amount)

        elif choice == "2":
            amount = float(input("Withdrawal amount : "))
            acc.withdraw(amount)

        elif choice == "3":
            acc.show_balance()

        elif choice == "4":
            save_accounts([acc.to_dict()])
            print(" Data saved to file. ")

        elif choice == "5":
            save_accounts([acc.to_dict()])
            print(" Goodbye! Data saved")
            break

        else:
            print("❌ Invalid option! ")


if __name__ == "__main__":
    main()
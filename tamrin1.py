def factorial_iterative(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("یک عدد صحیح مثبت وارد کنید: "))
result = factorial_iterative(num)
if result is None:
    print("خطا: عدد منفی مجاز نیست")
else:
    print(f"فاکتوریل {num} برابر است با: {result}")
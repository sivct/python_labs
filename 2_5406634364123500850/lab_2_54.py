def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("не целое число")








#1
a = get_int("a = ")
b = get_int("b = ")


while True:
    d = get_int("d = ")
    if d == 0:
        print("d не может быть 0")
    else:
        break

if (d > 0 and a > b) or (d < 0 and a < b):
    print("не попали в отрезок")
else:
    result = [x for x in range(a, b + 1, d) if x % 3 == 0]
    if result:
        print(*result)
    else:
        print("нету кратных трём")







# 2
n: int = get_int("n = ")
s, p = 0, 1
for i in range(1, n + 1):
    if i % 2 == 0:
        s += i
    else:
        p *= i
print(f"сумма чётных = {s}, произведение нечётных = {p}")



# 3
n: int = get_int("n = ")
print(sum(i*i for i in range(1, n + 1)))


# 4
k: int = get_int("k = ")
res = 1
for i in range(k, 0, -2):
    res *= i
print(res)




# 5
n, m = get_int("n = "), get_int("m = ")
print(*list(i for i in range(1, min(n, m) + 1) if n % i == 0 and m % i == 0))



# 6
#сумма нечётныъ до n
n: int = get_int("n = ")
print(sum(range(n+1)[1::2]))

#сумма первых n нечётных
print(sum(i + 2 for i in range(1, n+1))) 




# 7

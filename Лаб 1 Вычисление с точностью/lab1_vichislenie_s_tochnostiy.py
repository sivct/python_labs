def exp(x: float, eps: float) -> float:
    sum = 1.0
    res = sum
    step = 1


    while abs(sum) >= eps:
        sum *= x / step
        res += sum
        step += 1
    return res



eps = float(input("enter eps: "))
x = float(input("enter x: "))
print (f"e^{x} = {exp(5,eps)}, with acuracy = {eps}")


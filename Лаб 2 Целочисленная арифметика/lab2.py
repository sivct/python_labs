def _1(n: int) -> int:
    s = str(abs(n))
    return len(set(s))


def _2(n: int) -> bool:
    s = str(abs(n))
    return len(s) == len(set(s))


def is_simple_digit(n: int) -> bool:
    if n < 2: return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_sover(n: int) -> bool:
    sum: int = 0
    for i in range(1,n):
        if n % i == 0:
           sum += i
    return sum == n


def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def is_doublepalindrome(n: int) -> bool:
    return is_palindrome(n) and is_palindrome(n*n)

def is_armstrong(num: int) -> bool:
    s= str(num)
    n: int = len(s)
    return sum(i**n for i in s) == num




def _11(n: int) -> int:
    s = str(n)
    m = max(s)
    return int(m + str(n) + m)

def _17(n: int) -> list[int]:
    if n <= 0:
        return []
    if n== 1:
        return [1]
    res = [1, 1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res



def _24(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if is_palindrome(x)]


def _34(a:int, b:int) -> None:
    list = []
    for i in range(a,b+1):
        if is_sover(i):
            list.append(i)
    print(list)

def _35(a: int, b: int) -> list[int]:
    return [x for x in range(max(1,a), b + 1) if is_palindrome(x)]






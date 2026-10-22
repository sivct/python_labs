def fill_spiral(n: int) -> list[list[int]]:
    mtr = [[0] * n for _ in range(n)]
    

    r = n // 2
    c = n // 2    
    mtr[r][c] = 1
    num = 2

    size = n * n
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idx = 0
    counter = 1



    
    while num <= size:
        for _ in range(2):
            dr, dc = directions[idx]
            for _ in range(counter):
                if num > size:
                    break
                r += dr
                c += dc
                mtr[r][c] = num
                num += 1
            idx = (idx + 1) % 4
        counter += 1        
    return mtr







def print_mtr(mtr: list[list[int]]) -> None: #sprosil y ii kak vivesti s viravnivaniem
    n = len(mtr)
    cell_width = len(str(n * n)) + 2
    for r in mtr:
        print("".join(f"{val:>{cell_width}}" for val in r))


def sum_digits_rtriangle(mtr: list[list[int]]) -> tuple[int, list[int]]:
    n = len(mtr)
    res = []
    
    for i in range(n):
        for j in range(n):
            if i + j > n - 1:
                res.append(mtr[i][j])


    return sum(res)







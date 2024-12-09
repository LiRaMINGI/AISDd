x = int(input("Введите число x: "))
M=[]

for k in range(0, x + 1):
    for l in range(0, x + 1):
        for m in range(0, x + 1):
            value = (3 ** k) * (5 ** l) * (7 ** m)
            if value <= x and value > 0:
                M.append(value)

M.sort()
print(M)

def is_armstrong(numders):
    str_num = str(numders)
    power = len(str_num)
    total = sum(int(digit) ** power for digit in str_num)
    eiei = " + " .join(f"{digit}^{power}" for digit in str_num)
    return print(total == numders, f"{numders} = {total} = {eiei}")

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))
    
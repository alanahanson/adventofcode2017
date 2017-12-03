with open('solutions/solution1.txt') as f:
    digits = f.read().strip()

def sum_repeat_digits(offset):
    l = []
    for i, c in enumerate(digits):
        index_to_check = int((i + offset) % len(digits))
        if c == digits[index_to_check]:
            l.append(int(c))
    return sum(l)


print('Part 1', sum_repeat_digits(1))
print('Part 2', sum_repeat_digits(len(digits)/2))

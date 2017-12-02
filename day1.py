with open('solution1.txt') as f:
    read_data = f.read().strip()

l = []

for i, c in enumerate(read_data):
    try:
        if c == read_data[i+1]:
            l.append(int(c))
    except IndexError:
        if read_data[-1] == read_data[0]:
            l.append(int(read_data[0]))

print(sum(l))



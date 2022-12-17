h1 = 0
h2 = 0
h3 = 0
c = 0
p = 1

with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.replace('\n', '')

        if line:
            c += int(line)

        else:
            if c > h3:
                h3 = c

            if h3 > h2:
                tmp = h2
                h2 = h3
                h3 = tmp

            if h2 > h1:
                tmp = h1
                h1 = h2
                h2 = tmp

            c = 0

print(f'answer: {h1}')
print(f'answer: {h2}')
print(f'answer: {h3}')

print(h1 + h2 + h3)

infile = open('data.txt', 'r')    # open file
mean = 0
lines = 0
for line in infile:
    number = float(line)          # line is string
    mean = mean + number
    lines += 1
    print(f'number={number}')
mean = mean/lines
print(f'The mean value is {mean}')

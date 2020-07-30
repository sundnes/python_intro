pairs = []   # list of (n1, n2) pairs of numbers
with open('pairs.txt', 'r') as lines:
    for line in lines:
        words = line.split()
        for word in words:
            word = word[1:-1]  # strip off parentheses
            n1, n2 = word.split(',')
            n1 = float(n1);  n2 = float(n2)
            pair = (n1, n2)
            pairs.append(pair)

print(pairs)

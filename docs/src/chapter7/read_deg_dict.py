with open('deg2.txt', 'r') as infile:
    temps = {}                  # start with empty dict
    for line in infile:
        city, temp = line.split()
        city = city[:-1]        # remove last char (:)
        temps[city]  = float(temp)

print(temps)

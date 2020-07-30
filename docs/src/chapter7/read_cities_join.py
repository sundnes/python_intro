cities = {}
with open('cities.txt') as infile:
    for line in infile:
        words = line.split()
        name = ', '.join(words[:2])
        data = {'lat': float(words[2]),  'long':float(words[3])}
        data['pop'] = int(words[4])
        cities[name] = data

print(cities)

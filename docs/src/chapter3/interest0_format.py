years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in years:
    r = 5.0
    P = 100.0
    A = P * (1+r/100)**n
    print(f'{n:5d}{A:8.2f}')

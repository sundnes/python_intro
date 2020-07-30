P = 100
A_low = [P*(1+2.5/100)**n for n in range(11)]
A_high = [P*(1+5.0/100)**n for n in range(11)]

amounts = [A_low, A_high]  # list of two lists

print('The A_low list:\n', amounts[0])
print('The A_high list:\n',amounts[1])
print('3rd element in A_high:', amounts[1][2])  

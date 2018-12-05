Sweets = []

sweet_1 = int(input ('Enter the price of First Sweet:  ')[:-1])
Sweets.append(sweet_1)
sweet_2 = int(input ('Enter the price of Second Sweet:  ')[:-1])
Sweets.append(sweet_2)
sweet_3 = int(input ('Enter the price of Third Sweet:  ')[:-1])
Sweets.append(sweet_3)
sweet_4 = int(input ('Enter the price of Fourth Sweet:  ')[:-1])
Sweets.append(sweet_4)
sweet_5 = int(input ('Enter the price of Fifth Sweet:  ')[:-1])
Sweets.append(sweet_5)

print('Total: ' + str(sum(Sweets)) + 'p')
print('Average: ' + str(sum(Sweets)/5) + 'p')
print('Highest: ' + str(max(Sweets)) + 'p')
print('Lowest: ' + str(min(Sweets)) + 'p')
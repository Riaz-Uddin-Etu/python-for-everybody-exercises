num_list = list()

while True:
    numbers = input('Enter numbers: ')
    if numbers == 'done': break
    try:
        numbers = int(numbers)
    except:
        print('Invalid input')
        continue
    num_list.append(numbers)
    maximum = max(num_list)
    minimum = min(num_list)

print('Numbers entered:', num_list)
print('Maximum:', maximum)
print('Minimum:', minimum)

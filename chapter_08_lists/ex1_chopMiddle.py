# Exercise 1:

def chop(ls):
    del ls[0]
    del ls[-1]

def middle(ls):
    return ls[1:-1]

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6]

print(chop(letters))
print('After chop: ', letters)

new_numbers = middle(numbers)
print('original numbers: ', numbers)
print('new created numbers: ', new_numbers)

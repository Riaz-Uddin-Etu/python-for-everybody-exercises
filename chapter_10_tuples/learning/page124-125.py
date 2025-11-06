scores = {
    "Alice": 95,
    "Evan": 91,
    "Bob": 82,
    "George": 73,
    "Ian": 80,
    "Julia": 89,
    "Kevin": 92,
    "Laura": 76,
    "Charlie": 78,
    "Diana": 88,
    "Sam": 81,
    "Zane": 74,
    "Mason": 84,
    "Nina": 90,
    "Hannah": 97,
    "Oscar": 79,
    "Paula": 86,
    "Quentin": 94,
    "Rita": 77,
    "Xavier": 70,
    "Tina": 87,
    "Uma": 83,
    "Victor": 75,
    "Wendy": 93,
    "Fiona": 85,
    "Yara": 98
}

ls = list()
for k, v in scores.items():
    ls.append((v, k))

print('Before sort ===>\n', ls, '\n')

ls.sort(reverse=True)
print('After sort ===>\n', ls)

# By carefully constructing the list of tuples to have the value as the first element
# of each tuple, we can sort the list of tuples and get our dictionary contents sorted by value.
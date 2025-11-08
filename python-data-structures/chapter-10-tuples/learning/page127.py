# 10.9 List comprehension
int_as_str = ['23', '46', '97', '19']

# ls_int = []
# for x in int_as_str:
#     ls_int.append(int(x))

ls_int = [int(x) for x in int_as_str]

print(ls_int)
# Addition
print(sum(ls_int))

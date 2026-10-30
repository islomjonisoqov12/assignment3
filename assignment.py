def replace_value(values, index, new_value):
    values[index] = new_value

def find_first(values:list, target):
    for e in range(len(values)):
        if values[e] == target:
            return e
    return -1

def summarize(values):
    return (min(values), max(values), sum(values))

original = []

n_days = int(input("Enter the number of days: "))

for i in range(n_days):
    c_time = int(input("Enter cooking time in minutes: "))
    original.append(c_time)

updated = original[:]

c_index = int(input("Enter the index to correct: "))
new_val = int(input("Enter the new cooking time: "))

replace_value(updated, c_index, new_val)

target = int(input("Enter the cooking time to search for: "))
found1 = find_first(updated, target)

target_count = updated.count(target)

s_tuple = summarize(updated)

minimum, maximum, total = s_tuple

u_sorted = sorted(updated)


print(f'Original: {original}')
print(f'Updated: ', updated)
print(f'Sorted: ', u_sorted)
print(f'Minimum cooking time: {minimum} minutes')
print(f'Maximum cooking time: {maximum} minutes')
print(f'Total cooking time: {total} minutes')
if found1<0:
    print("Target not found")
else:
    print(f'First matching index: {found1}')

print(f'Matching values: {target_count}')

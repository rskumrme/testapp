import sys

# Create a sample collection test2
users = {'Hans': 'active1', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
print (sys.getsizeof(active_users))
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


print (active_users);
print (sys.getsizeof(active_users))
print (len(active_users))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

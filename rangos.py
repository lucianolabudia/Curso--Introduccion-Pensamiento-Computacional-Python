my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)

my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

print(my_range == my_other_range)

for i in my_range:
    print(i)

for i in my_other_range:
    print(i)

print(id(my_range))
print(id(my_other_range))

for i in range(0, 101, 2):
    print(i)
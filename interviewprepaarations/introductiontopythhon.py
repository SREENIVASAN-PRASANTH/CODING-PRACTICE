'''
a = 10
b = 10

print(a % b)


a = 10
b = 20.0
c = 10 + 4j

print(type(a))
print(type(b))
print(type(c))

'''

# a = 5
# print(float("5"))

# b = 7
# print(bool(-1))

# print(ord("A"))
'''a = "Prasanth yesterday"
    print(a[7:1:-2])
'''
'''
string1 = "My name is prasanth"
string2 = string1.replace("My", "His")
print(string2)
'''

tup = ('a', 'b', 'c', 'd', 'e')
tup_iter = iter(tup)

print("Inside loop:")

for index, item in enumerate(tup_iter):
    print(item)

    if index == 2:
        break

print("Outside loop:")
print(next(tup_iter))
print(next(tup_iter))




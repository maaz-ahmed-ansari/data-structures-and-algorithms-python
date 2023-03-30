num1 = 11
num2 = num1

print('--- Before num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))

num2 = 22

print('\n--- After num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))
print(
    """ That means:
    num2 now points to different integer whears num1 points to same
    Because integers are immutable
    """
    )


##################################### Dict

dict1 = {
    "value": 11
}

dict2 = dict1

print("--- Before value is update")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2["value"] = 22

print("\n--- After value is update")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

print(
    """ That means:
    Both dict1 and dict2 point to same location
    Dictionaries are mutable and thus can be changed
    Updating one's value will result in update of other as well
    """
    )

print(
    """
    What happens to dict2={'value': 11}?
    Here since we have changed the dict2 to {'value': 11},
    WHich points to this new location, so the previous location to which dict2 was pointing to 
    Is no longer acccessible since no variable points to it
    Thus Python will remove this garbage througha process called Garbage Collection.
    """
)
def add_items(n):
    # O(1) since only one operation involved
    return n + n + n


print(add_items(10)) 

# Even if n+n+n+n+n  --> O(1)
# Because for a given operation (as it is fixed in a given code)
# variation of n do not cause no. of operations to vary
# instead it is just a large number which needs to be operated on
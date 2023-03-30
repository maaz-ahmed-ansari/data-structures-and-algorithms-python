def print_items(n):
    # O(n)
    for i in range(n):
        print(i)

    # O(n)
    for j in range(n):
        print(j)

print_items(10)

# O(n) + O(n) = O(2n) =~ O(n)
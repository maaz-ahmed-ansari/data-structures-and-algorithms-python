def print_items(n):
    # O(n)
    for i in range(n):
        # O(n)
        for j in range(n):
            print(i,j) 

print_items(10)

# O(n) * O(n) = O(n^2)
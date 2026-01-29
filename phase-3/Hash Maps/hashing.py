n = int(input("Take the length of array: "))
arr = []
for i in range(n):
    arr.append(int(input()))

# Precompute
hash_map = [0] * n
for i in range(n):
    hash_map[arr[i]] += 1

q = int(input("Take the number of queries: "))
while q > 0:
    x = int(input("Enter the element to be searched: "))
    
    # Fetch
    if x < n:
        print(f"Frequency of {x} is {hash_map[x]}")
    else:
        print(f"Frequency of {x} is 0")
    
    q -= 1

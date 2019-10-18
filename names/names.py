import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# *** ORIGINAL *** O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# *** MVP *** O(n) for inserting names_1, O(log(n)) for searching names_2
# bst = BinarySearchTree('names')
# for name_1 in names_1:
#     bst.insert(name_1)
# # bst.bft_print(bst)
# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# *** STRETCH *** O(n)
names_dict = {}
for name_1 in names_1:
    names_dict[name_1] = name_1
for name_2 in names_2:
    if name_2 in names_dict:
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

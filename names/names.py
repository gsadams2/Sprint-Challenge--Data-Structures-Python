import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# duplicates = list(set(names_1) & set(names_2))

#& is the bitwise and.... compares each bit of the first operand to the corresponding bit of 
# the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, 
# the corresponding result bit is set to 0.


duplicates = []
for name in names_2:
    if name in names_1:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


#Old runtime is 7.396 seconds 


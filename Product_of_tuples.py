tuple1 = (1,5,3,6,7,9,-1,-2)
print(f"Given tuple: {tuple1}")
result = 1
count = 0
for i in tuple1:
    result *= tuple1[count]
    count += 1
print(f"Result of multiplication: {result}")
import matplotlib.pyplot as plt

genome = str(input("Enter genome: "))
skew = []

for i in range(len(genome)):
    skew.append(0)

for i in range(len(genome)):
    if i == 0:
        if genome[i] == 'G':
            skew[i] = 1
        elif genome[i] == 'C':
            skew[i] = -1
        else:
            skew[i] = 0
    else:
        if genome[i] == 'G':
            skew[i] = skew[i-1] + 1
        elif genome[i] == 'C':
            skew[i] = skew[i-1] - 1
        else:
            skew[i] = skew[i-1]

# Find min skew value
min_val = min(skew)

# Find all indices where skew is minimum
min_indices = [i + 1 for i, val in enumerate(skew) if val == min_val]

print("Minimum skew value:", min_val)
print("Positions with minimum skew:", min_indices)

# Plot
plt.plot(skew)
plt.scatter(min_indices, [min_val]*len(min_indices), color='red', label='Min Skew')
plt.title("Skew Diagram")
plt.xlabel("Position")
plt.ylabel("Skew Value")
plt.legend()
plt.grid(True)
plt.show()

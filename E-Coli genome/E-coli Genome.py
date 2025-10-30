import matplotlib.pyplot as plt

# --- Read genome exactly as in file ---
input_file = "E:\\bioinformatics-course-2024\Bioinformatics Algo'ms- An active learning approach\E-Coli genome\sequence_full.txt"

with open(input_file, "r") as f:
    genome = f.read()

# --- Compute skew ---
skew = [0] * len(genome)

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

# --- Find minimum skew and its positions ---
min_val = min(skew)
min_indices = [i + 1 for i, val in enumerate(skew) if val == min_val]

print("Minimum skew value:", min_val)
print("Positions with minimum skew:", min_indices)

# --- Plot ---
plt.plot(skew)
plt.scatter(min_indices, [min_val]*len(min_indices), color='red', label='Min Skew')
plt.title("Skew Diagram")
plt.xlabel("Position")
plt.ylabel("Skew Value")
plt.legend()
plt.grid(True)
plt.show()

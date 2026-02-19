import matplotlib.pyplot as plt

iterations = []
probabilities = []

# read the data from the txt file
with open("../data/results.txt", "r") as f:
    next(f)  # skip header line
    for line in f:
        i, p = line.strip().split(",")
        iterations.append(int(i))
        probabilities.append(float(p))

# plot the data

plt.figure()
plt.plot(iterations, probabilities, marker='o', label="Estimated probability")
plt.axhline(y=1/11, color='red', linestyle='--', label="Theoretical probability (1/11)")
plt.xscale("log")
plt.xlabel("Number of simulations (log scale)")
plt.ylabel("P(missing number = 8)")
plt.title("Convergence of Probability (Ladybug Clock Puzzle)")
plt.grid(True)
plt.legend()

# save at different y-limits
plt.savefig("../plots/plot_no_y-limit.png", dpi = 300)
plt.ylim(0.06, 0.12)
plt.savefig("../plots/plot_y-limit_0.06-0.12.png", dpi = 300)
plt.ylim(0.08, 0.10)
plt.savefig("../plots/plot_y-limit_0.08-0.10.png", dpi = 300)
plt.ylim(0.0899, 0.0919)
plt.savefig("../plots/plot_y-limit_0899-0.0919.png", dpi = 300)

print("Plots finished. Results saved to plots")
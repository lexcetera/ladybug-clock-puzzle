import math

# theoretical probability
true_prob = 1 / 11

# read the simulation results
trials = []
probs = []

with open("../data/results.txt") as file:
    next(file)  
    for line in file:
        t, p = line.strip().split(",")
        trials.append(int(t))
        probs.append(float(p))

# calculate standard error and difference from 1/11
std_errors = []
distance = []

for n, p in zip(trials, probs):
    std_errors.append(math.sqrt(p * (1 - p) / n))
    distance.append(p - true_prob)

# display results and save file
print("Trials\tProbability\tStd Error\tdistance vs 1/11")
for t, p, se, d in zip(trials, probs, std_errors, distance):
    print(f"{t}\t{p:.6f}\t\t{se:.6f}\t\t{d:.6f}")

with open("../data/errors.txt", "w") as f:
    f.write("trials,probability,std_error,distance_to_1/11\n")
    for t, p, se, d in zip(trials, probs, std_errors, distance):
        f.write(f"{t},{p:.6f},{se:.6f},{d:.6f}\n")

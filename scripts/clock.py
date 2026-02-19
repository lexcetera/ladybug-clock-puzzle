import random

clock = 12
done = [12]
target = [1,2,3,4,5,6,7,8,9,10,11,12]
missing = []

iterations = 1000000 # max value 

# checkpoints where probability values are saved
checkpoints = [1, 10, 100, 1000, 10000, 100000, 1000000]

num_to_count = 6 # this could be any integer from 1 to 11
num_count = 0

# open file for saving results
with open("../data/results.txt", "w") as f:
    f.write("iterations,probability_missing\n")

    for i in range(1, iterations + 1):

        while len(done) < 11:
            clock = clock + random.choice([-1, 1])

            if clock == 13:
                clock = 1
            if clock == 0:
                clock = 12

            if clock not in done:
                done.append(clock)

        missing_number = list(set(target) - set(done))[0]

        if missing_number == num_to_count:
            num_count += 1

        # save probability at checkpoints
        if i in checkpoints:
            probability = num_count / i
            f.write(f"{i},{probability:.6f}\n")

        # reset for next iteration
        done = [12]
        clock = 12

print("Simulation finished. Results saved to results.txt")

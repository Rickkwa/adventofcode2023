def predict_next(history):
    # print(f"Predict called with {history}")
    diffs = []
    for i in range(len(history) - 1):
        diffs.append(history[i + 1] - history[i])
    if any(diffs):
        return history[0] - predict_next(diffs)
    else:
        return history[0]


histories = []
with open("input.txt", "r") as fp:
    for line in fp:
        histories.append([int(x) for x in line.strip().split(" ")])

# print(histories)

total = 0
for history in histories:
    n = predict_next(history)
    print(n)
    total += n

print("total", total)

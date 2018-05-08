# W = []

# for i in range(100):
#   line = raw_input().split()
#   score = int(line[1])
#   max_score = int(line[5])
#   if max_score == 0:
#     continue
#   res = 1.0*score/max_score
#   if score > 0:
#     res += 0.2
#   W.append(res)
# print "Score:", 1.0*sum(W)/len(W)


W, S = [], []
for i in range(100):
    line = raw_input()[:-1].split()
    score = int(line[-1])
    step = line[-3][:-1]
    step = int(step)
    W.append(score)
    S.append(step)
print("Score:", 1.0 * sum(W) / 100.0, "Step:", 1.0 * sum(S) / 100.0)

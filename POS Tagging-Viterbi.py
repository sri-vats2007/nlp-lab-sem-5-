words = ["the", "dog", "barks"]
tags = ["D", "N", "V"]
start = {"D": 0.6, "N": 0.3, "V": 0.1}
trans = {
"D": {"D": 0.05, "N": 0.90, "V": 0.05},
"N": {"D": 0.20, "N": 0.20, "V": 0.60},
"V": {"D": 0.30, "N": 0.30, "V": 0.40}
}
emit = {
"the": {"D": 0.9, "N": 0.05, "V": 0.05},
"dog": {"D": 0.05, "N": 0.9, "V": 0.05},
"barks": {"D": 0.05, "N": 0.05, "V": 0.9}
}
dp = [{}]
back = [{}]
for tag in tags:
dp[0][tag] = start[tag] * emit[words[0]][tag]
back[0][tag] = None
for i in range(1, len(words)):
dp.append({})
back.append({})
for tag in tags:
candidates = [(dp[i-1][prev] * trans[prev][tag] *
emit[words[i]][tag], prev) for prev in tags]
dp[i][tag], back[i][tag] = max(candidates)
last = max(tags, key=lambda t: dp[-1][t])
path = [last]
for i in range(len(words)-1, 0, -1):
path.append(back[i][path[-1]])
path.reverse()
print(list(zip(words, path)))

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [10, 25, 50, 120]
new_ranked = []

for ele in ranked:
    if ele not in new_ranked:
        new_ranked.append(ele)
print(new_ranked)
#    new_ranked = sorted(list(set(ranked)), reverse=True)
alice_rank = []
for score in player:
    while new_ranked and score >= new_ranked[-1]:
        new_ranked.pop()
    alice_rank.append(len(new_ranked)+1)

print(alice_rank)

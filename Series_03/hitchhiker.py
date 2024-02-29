hitchhikers = int(input())

max_score = 0

for h in range(hitchhikers // 2):
    score = float(input())
    if score > max_score:
        max_score = score

for h in range(hitchhikers // 2, hitchhikers):
    score = float(input())
    if score > max_score:
        print(score)
        break
else:
    print(score)

moves = int(input())
arr = list(map(int, input().split()))
pos = 0
count = 0
for i in range(moves):
    pos = pos + arr[i]
    if pos == 0:
        count += 1
print(count)

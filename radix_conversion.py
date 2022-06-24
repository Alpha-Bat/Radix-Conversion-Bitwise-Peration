N, B = list(map(str,input().split()))
B = int(B)
ans = 0
for idx, n in enumerate(N):
    if n in ['0','1','2','3','4','5','6','7','8','9']:
        ans += int(n) * B ** (len(N) - idx - 1)
    else:
        ans += (ord(n)-55) * B ** (len(N) - idx - 1)
print(ans)

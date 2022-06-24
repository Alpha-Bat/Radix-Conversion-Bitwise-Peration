N = []
ANS = []
while True :
    n = int(input())
    if n == 0 :
        break
    N.append(n)
for n in N :
    ans = 0
    ans += n % 10
    if n // 10 != 0 :
        n = n // 10
        ans += (n % 10) * 2
    if n // 10 != 0 :
        n = n // 10
        ans += (n % 10) * 6
    if n // 10 != 0 :
        n = n // 10
        ans += (n % 10) * 24
    if n // 10 != 0 :
        n = n // 10
        ans += (n % 10) * 120
    print(ans)

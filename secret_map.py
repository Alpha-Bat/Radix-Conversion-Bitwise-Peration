def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans = ''
        for idx, j in enumerate(str(bin(arr1[i] | arr2[i]))[::-1]):
            if j == '1':
                ans += '#'
            elif j == '0':
                ans += ' '
            elif j == 'b':
                break
        while len(ans) < n :
            ans += ' '
        answer.append(ans[::-1])
    return answer

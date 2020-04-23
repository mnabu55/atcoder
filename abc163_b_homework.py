n, m = map(int, input().split())
day_list = list(map(int, input().split()))

sum_day = sum(day_list)
remain_day = n - sum_day
if remain_day >= 0:
    print(remain_day)
else:
    print(-1)
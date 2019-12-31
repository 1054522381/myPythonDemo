# 打印0到100，跳过50
i = 0
sum = 0
while i < 100:
    if i == 50:
        i += 1
        # 跳出本次循环
        continue
    print('i=%s' % i)
    sum += i
    i += 1
print('sum=%s' % sum)


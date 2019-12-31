# 打印0到100
i = 0
sum = 0
while i < 100:
    if i == 50:
        # 跳出循环
        break
    print('i=%s' % i)
    sum += i
    i += 1
print('sum=%s' % sum)


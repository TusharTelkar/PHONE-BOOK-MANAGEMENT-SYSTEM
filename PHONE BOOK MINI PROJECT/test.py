c = [101, 102]
r = [103, 107]
m = 102
while True:
    # if m in c:
    #     m += 1
    # else:
    #     break
    if m in r:
        m += 1
        if m in c:
            m += 1
    else:
        break

print(m)

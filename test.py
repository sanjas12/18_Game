l = [False, False, False, False, False, False, False, False, False]
l = [False, False, True, False, False, False, False, True, False]
print([(i, v) for i, v in enumerate(l) if v])
print(sum(l))
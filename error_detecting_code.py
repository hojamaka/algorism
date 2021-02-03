s = "5555555555554444"
w = 1; t = 0
for i in range(len(s) - 1, -1, -1):
    d = w * int(s[i])
    if d > 9:
        d -= 9
    t += d
    w = 3 - w
if t % 10 == 0:
    print("有効")
else:
    print("無効")

n = int(input())
f = 1
i = 0
f1 = f
fn = 0
a = [1, 1]
# fn = f + f1
while i < n:
    fn = f + f1
    f = f1
    f1 = fn
    i += 1

    a.append(fn)
print(a)
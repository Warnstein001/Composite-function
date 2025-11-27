def f(x):
    return x * x

def g(x):
    return x - 3

# f(g(x))
def composite(x):
    tmp = g(x)
    return f(tmp)

print(composite(3))
print(composite(4)) 
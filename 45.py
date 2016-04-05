def triangle(n):
    return n * (n + 1) / 2

def pentagon(n):
    return n * (3 * n - 1) / 2

def hexagon(n):
    return n * (2 * n - 1)

def is_triangular(n):
    global last_t_i
    i = last_t_i
    while True:
        t = triangle(i)
        if t == n:
            last_t_i = i
            return True
        if t > n:
            last_t_i = i - 1
            return False
        i += 1

def is_pentagonal(n):
    global last_p_i
    i = last_p_i
    while True:
        p = pentagon(i)
        if p == n:
            last_p_i = i
            return True
        if p > n:
            last_p_i = i - 1
            return False
        i += 1

last_t_i = 285
last_p_i = 165


i = 144
while True:
    n = hexagon(i)
    if is_pentagonal(n) and is_triangular(n):
        print n
        break
    i+= 1

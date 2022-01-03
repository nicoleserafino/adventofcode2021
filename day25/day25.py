m = [a.strip() for a in open("2021/day25/input.txt")]
h, w = len(m), len(m[0])

a = {(r,c): m[r][c] for r in range(h)
                    for c in range(w)
                    if m[r][c] != '.'}

for t in range(1000):
    def move(new, x): return {new(*pos) if
        new(*pos) not in a and fish==x else
        pos:fish for pos,fish in a.items()}

    b = a.copy()
    a = move(lambda r,c: (r, (c+1)%w), '>')
    a = move(lambda r,c: ((r+1)%h, c), 'v')

    if a == b: print(t+1); break
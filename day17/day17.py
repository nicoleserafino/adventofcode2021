from re import findall

def sim(vx, vy, px=0, py=0):
    if px > x2 or py < y1: return 0
    if px >= x1 and py <= y2: return 1
    return sim(vx-(vx>0), vy-1 , px+vx, py+vy)

def Main():
    global x1, x2, y1, y2
    x1,x2,y1,y2 = map(int, findall(r'-?\d+', open("2021/day17/input.txt", 'r').read()))

    hits = [sim(x,y) for x in range(1, 1+x2)
                 for y in range(y1, -y1)]

    print(f'Part 1: {y1*(y1+1)//2}\nPart 2: {sum(hits)}')

if __name__ == '__main__':
    Main()
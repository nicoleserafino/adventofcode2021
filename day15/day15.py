from time import perf_counter as pc

def inr(pos, arr):
	return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

def find_risk(ll):
	q = [(0, 0, 0)]
	costs = {}
	while True:
		cost,x,y = q[0]
		if x==len(ll)-1 and y==len(ll[0])-1: 
			return cost
		q=q[1:]
		for xx,yy in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
			if inr((xx,yy),ll):
				nc = cost + ll[xx][yy]
				if (xx,yy) in costs and costs[(xx,yy)]<=nc:
					continue
				costs[(xx,yy)]=nc
				q.append((nc,xx,yy))
		q = sorted(q)

def expand_cave(ll):
	expanded = [[0 for _ in range(5*len(ll[0]))] for _ in range(5*len(ll))]
	for x in range(len(expanded)):
		for y in range(len(expanded[0])):
			dist = x//len(ll) + y//len(ll[0])
			newval = ll[x%len(ll)][y%len(ll[0])]
			for _ in range(dist):
				newval+=1
				if newval==10:
					newval=1
			expanded[x][y] = newval
	return expanded

def Main():
	data = [[int(y) for y in x] for x in open('2021/day15/input.txt').read().strip().split('\n')]
	
	# Part 1
	start1 = pc()
	p1 = find_risk(data)
	t1 = pc() - start1

	# Part 2
	start2 = pc()
	expanded_cave = expand_cave(data)
	p2 = find_risk(expanded_cave)
	t2 = pc() - start2

	print(f"Part 1: {p1} in {t1} seconds\nPart 2: {p2} in {t2} seconds")

if __name__ == '__main__':
    Main()
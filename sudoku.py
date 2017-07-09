from collections import defaultdict
rows = defaultdict(list)
cols = defaultdict(list)
vals = {}
		
def main():
	c = 0
	for i in range(9):
		for j in range(9):
			vals[(i,j)] = c
			c += 1

	for i in range(9):
	#	for j in range(9):
		rows[i] = [vals[(i,j)] for j in range(9)]# .append(vals[(i,j)])
	#		cols[i].append(vals[(j,i)])

	for i in range(9):
		print(rows[i])

	c = 0
	for i in range(9):
		for j in range(9):
			vals[(i,j)] = 100-c
			c += 1

	for i in range(9):
		print(rows[i])

main()
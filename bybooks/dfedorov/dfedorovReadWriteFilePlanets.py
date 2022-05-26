with open('planets.txt') as f:
	lines = f.readlines()
	lines.sort()
	with open('planets_sorted.txt', 'w') as fo:
		fo.writelines(lines)
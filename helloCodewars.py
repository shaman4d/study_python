x = 0
y = 12
name = x or y
print(name)

'''
def group_by_commas(n):
	s = str(n)
	g = []
	while s:
		g.append(s[-3:])
		s = s[:-3] 
		return ','.join(reversed(g))
'''
'''

def group_by_commas(n):
    return '{:,}'.format('1000000')

print(group_by_commas(1))
print(group_by_commas(10))
print(group_by_commas(100))
print(group_by_commas(1000))
print(group_by_commas(10000))
print(group_by_commas(100000))
print(group_by_commas(1000000))
print(group_by_commas(31123777))
'''


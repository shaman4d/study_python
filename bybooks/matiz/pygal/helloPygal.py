import random
import pygal

results = []
for r in range(0,10000):
	results.append(random.randint(1,6))

# print(results)

freq = []
for i in range(1,7):
	freq.append(results.count(i))
print(freq)

hist = pygal.Bar()
hist._title = "Result of rolling one D6"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Freq'
hist.add('D6',freq) 
hist.render_to_file('visual.svg')

import matplotlib.pyplot as plt

'''
input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5, zorder=0)
plt.title('Square numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Sqr. of Value', fontsize=14)
plt.tick_params(labelsize=10, size=10)
plt.scatter(input_values, squares, zorder=1, color='red',edgecolor='blue', s=400)
'''


#'''
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values,edgecolors='none', s=40, cmap=plt.cm.Blues)
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
#'''

plt.show()


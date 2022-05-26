import matplotlib.pyplot as plt
import random


class Walker():
    def __init__(self):
        self.x_origin = 0
        self.y_origin = 0
        self.x_steps = [0]
        self.y_steps = [0]

    def makePath(self, steps):
        counter = 0
        while counter < steps:
            counter += 1
            self.x_origin += random.randint(-1, 1) * random.randint(0, 10)
            self.y_origin += random.randint(-1, 1) * random.randint(0, 10)
            self.x_steps.append(self.x_origin)
            self.y_steps.append(self.y_origin)


walker = Walker()
walker.makePath(10000)

plt.figure(dpi=144)
plt.plot(walker.x_steps, walker.y_steps)
plt.scatter(walker.x_steps, walker.y_steps, s=1, c=walker.x_steps, cmap=plt.cm.Blues, edgecolor='none')
plt.show()

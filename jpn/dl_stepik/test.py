class Neuron:

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        return self.f(sum(map(lambda w,x: w*x, self.w, self.x)))

    def backlog(self):
        return self.x


# YOUR CODE HERE

def Test():
    test_neuron = Neuron([2, 3, 4, 5, 6], lambda x: x * x)
    if (test_neuron.forward([1, 2, 3, 4, 5]) == 4900 and test_neuron.backlog() == [1, 2, 3, 4, 5]):
        print("Задание успешно выполнено!")
    else:
        print("Ошибка в решении!")


Test()

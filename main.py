import numpy as np


class Neuron:
    def __init__(self):
        self._weight = np.random.random()
        self._bias = np.random.random()
        self.learning_rate = 0.0001
        self.epoch = 10000

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_bias(self):
        return self._bias

    def set_bias(self, bias):
        self._bias = bias

    def sigma(self, data):
        return data * self.get_weight() + self.get_bias()


class Perceptron(Neuron):
    def __init__(self):
        super(Perceptron, self).__init__()

    def fit(self, x_train, y_train):
        pass

    def predict(self, x_test):
        pass


if __name__ == '__main__':
    print('Py-------->Charm')
    x = Neuron()
    print(x.get_bias())

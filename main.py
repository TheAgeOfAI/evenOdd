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

    def get_values(self):
        print(f"Weight is : {self.get_weight()}")
        print(f"Bias is : {self.get_bias()}")


class Perceptron(Neuron):

    def __init__(self):
        super(Perceptron, self).__init__()

    def fit(self, x_train, y_train):

        for _ in range(self.epoch):
            for i in range(len(x_train)):
                prediction = self.predict_train(x_train[i])

                error = y_train[i] - prediction

                self.set_weight(self.get_weight() + self.learning_rate * error * x_train[i])
                self.set_bias(self.get_bias() + self.learning_rate * error)

    def predict_train(self, x_test):

        result = self.sigma(x_test)
        return 1 if result >= 0 else 0

    def predict(self, x_test):
        predictions = []
        for i in range(len(x_test)):
            predictions.append(self.predict_train(x_test[i]))
        return predictions

if __name__ == '__main__':

    x = Perceptron()
    x.get_values()
    n = 10000
    X_train = np.arange(n).reshape(-1, 1)  # Input features
    Y_train = np.array([0, 1] * (n // 2))
    x.fit(X_train, Y_train)
    x.get_values()
    X_test = np.array([[10], [11], [12], [13], [14], [15]])
    y_test = np.array([0, 1, 0, 1, 0, 1])

    prediction = x.predict(X_test)
    print(prediction)

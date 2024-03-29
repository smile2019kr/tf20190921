import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dlearn.perceptron import Perceptron
from matplotlib.colors import ListedColormap

class IrisModel:
    def __init__(self):
        self.iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                                header=None)
        # setosa 와 versicolor 선택
        t = self.iris.iloc[0:100, 4].values
        self.y = np.where(t == 'Iris-setosa', -1, 1)
        # 꽃받침 길이와 꽃잎을 추출
        self.X = self.iris.iloc[0:100, [0,2]].values
        self.classifier_algorithm = Perceptron(eta = 0.1, n_iter=10)

    def get_iris(self):
        return self.iris
    def get_X(self):
        return self.X
    def get_y(self):
        return self.y

    def draw_scatter(self):
        X = self.X
        plt.scatter(X[:50,0], X[:50,1],
                    color = 'red',
                    marker = 'o',
                    label = 'setosa')
        plt.scatter(X[50:100,0], X[50:100,1],
                    color='blue',
                    marker='x',
                     label='versicolor')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc = 'upper left')
        plt.show()

    def plot_decision_regions(self):
        X = self.X
        y = self.y
        classifier = Perceptron(eta=0.1, n_iter=10)
        classifier.fit(X, y)
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])
        # 결정경계 그리기
        x1_min, x1_max = X[:,0].min() -1, X[:,0].max() +1
        x2_min, x2_max = X[:,1].min() -1, X[:,1].max() +1
        resolution = 0.2
        """
        numpy모듈의 arrange 함수는 반열린 구간 [start, stop]에서 
        step의 크기만큼 일정하게 떨어져있는 숫자들을 
        array 형태로 반환해주는 함수
        
        meshgrid 명령은 사각형 영역을 구성하는 
        가로축의 점들과 세로축의 점을 나타내는 두 벡터를 인수로 받아서
        이 사각형 영역을 이루는 조합을 출력한다
        결과는 그리드 포인트의 x값만을 표시하는 행렬과 y값만을 표시하는 행렬 두개로 분리하여 출력한다
        """

        xx1, xx2 = np.mashgrid(np.arrange(x1_min, x1_max, resolution),
                               np.arrange(x2_min, x2_max, resolution))
        Z = classifier.predict(np.array([xx1.rabel(), xx2.rabel()]).T)
        Z = Z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        #샘플의 산점도
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x = X[y == cl, 0],
                        y = X[y == cl, 1],
                        alpha=0.8,
                        c = colors[idx],
                        label = cl,
                        edgecolors = 'black')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc = 'upper left')
        plt.show()

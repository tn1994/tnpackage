import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE
import sklearn.datasets
import datetime

"""ref:https://qiita.com/t-iguchi/items/a0bb8a5f273b319e5755"""
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime('%Y_%m_%d_%H_%M_%S')

digits, label = sklearn.datasets.load_digits(return_X_y=True)
digits = digits / 255


def hoge():
    """ref:https://blog.imind.jp/entry/2019/06/25/004531"""
    digits2d = TSNE(n_components=2).fit_transform(digits)
    f, ax = plt.subplots(1, 1, figsize=(10, 10))
    for i in range(10):
        target = digits2d[label == i]
        ax.scatter(x=target[:, 0], y=target[:, 1], label=str(i), alpha=0.5)
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
    # plt.show(block=True)
    # plt.show(block=True)
    # plt.interactive(False)
    # plt.savefig(f'./archive/plt/{timestamp}.png')
    plt.savefig(f'app/archive/plt/{timestamp}.png')


def hogehoge():
    mnist = fetch_openml('mnist_784', version=1)
    mnist.target = mnist.target.astype(int)

    idx = np.random.permutation(60000)[:10000]  # 60000の数字をランダムに置き換えて、10000個抽出してインデックスを作成

    X = mnist['data'][idx]
    y = mnist['target'][idx]

    print(X.shape)


if __name__ == '__main__':
    hoge()

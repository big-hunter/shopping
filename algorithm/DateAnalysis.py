import numpy as np
import matplotlib.pyplot as plt
import algorithm.KNN as KNN


def draw(dating_dat_mat, label):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(dating_dat_mat[:, 1], dating_dat_mat[:, 2])
    ax.scatter(dating_dat_mat[:, 1], dating_dat_mat[:, 2],
               15.0 * np.array(label), 15.0 * np.array(label))
    plt.show()


if __name__ == '__main__':
    return_mat, label_vector = KNN.file_to_matrix("datingTestSet2.txt")
    draw(return_mat, label_vector)

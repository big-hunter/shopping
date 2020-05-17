import numpy as np
import operator
import matplotlib.pyplot as plt

'''
prepare data
'''


def create_set():
    group = np.array([
        [1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


'''
    show to point
'''


def pic(x_aix, y_aix):
    plt.scatter(x_aix, y_aix, c='b')
    plt.xlabel(xlabel="x")
    plt.ylabel(ylabel="y")
    plt.grid()
    plt.show()


'''
 in_x  value used for classify 
 data_x train set
 labels
 k use for select neighbor
'''


def classify(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = np.tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sort_distance_index = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sort_distance_index[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sort_class_count = sorted(class_count.items(), key=operator.itemgetter(1),
                              reverse=True)
    return sort_class_count[0][0]


def auto_norm(dataSet):
    min_val = dataSet.min(0)
    max_val = dataSet.max(0)
    ranges = max_val - min_val
    norm_data_set = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    norm_data_set = dataSet - np.tile(min_val, (m, 1))
    norm_data_set = norm_data_set / np.tile(ranges, (m, 1))  # element wise divide
    return norm_data_set, ranges, min_val


def file_to_matrix(file_name):
    fr = open(file_name)
    array_of_lines = fr.readlines()
    number_of_lines = len(array_of_lines)
    return_mat = np.zeros((number_of_lines, 3))
    class_label_vector = []
    index = 0
    for line in array_of_lines:
        line = line.strip()
        lines_from_line = line.split('\t')
        return_mat[index, :] = lines_from_line[0: 3]
        class_label_vector.append(int(lines_from_line[-1]))
        index += 1
    return return_mat, class_label_vector


def dating_class_test():
    ho_ratio = 0.10
    dating_data_mat, dating_labels = file_to_matrix("datingTestSet2.txt")
    norm_mat, ranges, min_val = auto_norm(dating_data_mat)
    m = norm_mat.shape[0]
    num_test_vecs = int(m * ho_ratio)
    error_count = 0
    for i in range(num_test_vecs):
        classify_result = classify(norm_mat[i, :], norm_mat[num_test_vecs:m, :], dating_labels[num_test_vecs: m], 3)
        print("the classify came back with %d , the real answer is %d", (classify_result, dating_labels[i]))
        if classify_result != dating_labels[i]:
            error_count += 1.0
    print("the total error rate is: %f %", (float(error_count) / float(num_test_vecs)))


def classify_person():
    result = ["not at all", "in small does", "in large does"]
    games = input("percentage of time spent playing video games")
    miles = input("frequent filter miles earned per year")
    ice_cream = input("percentage of time spent ice_cream per years")
    dating_data_mat, dating_labels = file_to_matrix("datingTestSet2.txt")
    norm_mat, ranges, min_val = auto_norm(dating_data_mat)
    in_arr = np.array([miles, games, ice_cream])
    classif_result = classify(in_arr, norm_mat, dating_labels, k)


if __name__ == '__main__':
    dating_class_test()

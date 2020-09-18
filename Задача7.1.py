
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for l in range(len(self.list_2[i])):
                matr[i][l] = self.list_1[i][l] + self.list_2[i][l]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(l) for l in i]) for i in matr]))



my_matrix = Matrix([[8, 5, 3],
                    [8, 13, 11],
                    [25, 41, 55]],
                   [[65, 3, 9],
                    [6, 1, 63],
                    [21, 7, 101]])
print(my_matrix.__add__())
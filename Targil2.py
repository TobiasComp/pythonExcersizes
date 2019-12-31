import sys

def unique_one(L):
    return set(L)


def unique_two(L):
    newList = []
    for item in L:
        if item not in newList:
            newList.append(item)
    return newList

def matrix_build_5():
    matrix = []
    for lis in range(5):
        temp_list = []
        for number in range(5):
            if lis == number:
                temp_list.append(1)
            else:
                temp_list.append(0)
        matrix.append(temp_list)
    return matrix


def matrix_v():
    matrix = []
    for lis in range(3):
        temp_list = []
        for number in range(5):
            temp_list.append(0)
        matrix.append(temp_list)
    for lis in range(3):
        matrix[lis][lis] = 1
        matrix[lis][-(lis+1)] = 1
    return matrix


def matrix_custom_size(size):
    matrix = []
    for lis in range(size):
        temp_list = []
        for number in range(size):
            if lis == number:
                temp_list.append(1)
            else:
                temp_list.append(0)
        matrix.append(temp_list)
    return matrix



def main():
    # L = ['Moshe',"Shimon", "Aharon", "David", "Aharon"]
    # print(L)
    # print(unique_one(L))
    # print(unique_two(L))
    # print(matrix_build_5())
    # print(matrix_v())
    # print(matrix_custom_size(3))
    print(sys.argv)



if __name__ == "__main__":
    main()

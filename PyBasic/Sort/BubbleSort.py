from __future__ import print_function

array = [12, 5, 13, 8, 9, 65]


def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i + 1]:
                sorted = False
                bad_list[i], bad_list[i + 1] = bad_list[i + 1], bad_list[i]


bubble(array)
print(array)

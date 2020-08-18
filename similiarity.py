import math


def remove_comment(file_string):
    file_string = file_string.split("\n")
    tes = ""
    index = 0
    for x in file_string:
        if "//" in x:
            index += 1
            continue
        if index < (len(file_string) - 1):
            tes = tes + x + '\n'
        else:
            tes = tes + x
        index += 1
    return tes


# membagi baris menjadi kata
# translation table adalah
# global variable untuk mapping
# huruf besar dan kecil dan tanda baca ke spasi

# translation_table = str.maketrans(string.punctuation + string.ascii_uppercase,
#                                   " " * len(string.punctuation) + string.ascii_lowercase)


# mengembalikan list kata
# dalam file

def get_words_from_line_list(text):
    # text = text.translate(translation_table)
    word_list = text.split()
    list_stop_word = ['#include']
    word_list = [x for x in word_list if x not in list_stop_word]

    return word_list


def get_line_from_line_list(text):
    word_list = text.split('\n')
    # todo bagian penting
    while "" in word_list:
        word_list.remove("")
    return word_list


def count_line_frequency(line_list_1, line_list_2):
    # todo bagian penting
    same_line = list(filter(lambda x: x in line_list_1, line_list_2))
    return (2 * len(same_line)) / (len(line_list_1) + len(line_list_2))


# menghitung frekuensi setiap kata

def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D


# mengembalikan kamus pasangan
# (kata, frekuensi)

def word_frequencies_for_file(filename):
    line_list = filename
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)

    # print("file", filename, ":", )
    # print(len(line_list), "lines,", )
    # print(len(word_list), "words,", )
    # print(len(freq_mapping), "distinct word")

    return freq_mapping


# mengembalikan hasil perkalian dua dokumen(titik)


def dot_prduct(D1, D2):
    Sum = 0.0
    for key in D1:
        if key in D2:
            Sum += (D1[key] * D2[key])
    return Sum


# mengembalikan sudut dalam radian
# diantara dua vector

def vector_angle(D1, D2):
    numerator = dot_prduct(D1, D2)
    denominator = math.sqrt(dot_prduct(D1, D1) * dot_prduct(D2, D2))
    return math.acos(numerator / denominator)


def line_frequencies_for_file(filename_1, filename_2):
    line_list_1 = filename_1
    separate_list_1 = get_line_from_line_list(line_list_1)
    line_list_2 = filename_2
    separate_list_2 = get_line_from_line_list(line_list_2)
    freq_line = count_line_frequency(separate_list_1, separate_list_2)
    return freq_line


def line_frequencies_for_fileV2(filename_1, filename_2):
    line_list_1 = filename_1
    separate_list_1 = get_words_from_line_list(line_list_1)
    line_list_2 = filename_2
    separate_list_2 = get_words_from_line_list(line_list_2)
    freq_lineV2 = count_word_frequencyV2(separate_list_1, separate_list_2)
    return freq_lineV2


def count_word_frequencyV2(line_list_1, line_list_2):
    line_list_1 = join_with_n2(line_list_1)
    line_list_2 = join_with_n2(line_list_2)
    same_line = list(filter(lambda x: x in line_list_1, line_list_2))
    return (2 * len(same_line)) / (len(line_list_1) + len(line_list_2))


def join_with_n2(line_list):
    data = list()
    size = len(line_list)
    for x in range(size):
        if x == size - 1:
            break
        data.append(str(line_list[x] + " " + line_list[(x + 1)]))
    return data


def documentSimiliarity(filename_1, filename_2):
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    sorted_line_list = line_frequencies_for_file(filename_1, filename_2)
    sorted_line_list = sorted_line_list * 100

    sorted_line_list_n2 = line_frequencies_for_fileV2(filename_1, filename_2) * 100
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    distance = abs(((rad2deg(distance) / 90) * 100) - 100)
    # average_percentage = (sorted_line_list + (abs(((np.rad2deg(distance) / 90) * 100) - 100))) / 2
    list = [distance, sorted_line_list, sorted_line_list_n2]
    return list


def rad2deg(radian):
    return radian * (180 / math.pi)

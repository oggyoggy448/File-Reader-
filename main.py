"""
A text file reader

This project calculates the following things from a file

total number of lines
total number of words
largest word alphabetically
smallest word alphabetically

"""


def file_reader(filename: str):
    """
    return file
    :param filename: name of the file which you want to open
    :return: file object
    """
    file = None
    try:
        file = open(filename)
    except FileNotFoundError:
        print("Error, file not found")
        exit()
    return file


def file_lines_calculator(file):
    """
    returns the total numbers of lines in a file
    :param file:
    :return:
    """
    return len(file.readlines())


def words_counter(file):
    """
    counts total number of words in a file
    :param file:
    :return:
    """
    word_counter = 0
    for line in file:
        line = line.strip()
        word_counter += len(line.split())
    return word_counter


def largest_word_counter(file):
    """
    largest word finder alphabetically
    :param file: file object
    :return: str
    """
    largest_word = []

    for line in file.readlines():
        line = line.strip()
        for word in line.split():
            if word not in largest_word:
                largest_word.append(word.lower())

    return max(largest_word)


def smallest_word_counter(file):
    """
    smallest word finder alphabetically
    :param file:
    :return: str
    """
    smallest_word = []

    for line in file.readlines():
        line = line.strip()
        for word in line.split():
            if word not in smallest_word:
                smallest_word.append(word.lower())
    return min(smallest_word)


if __name__ == '__main__':
    file_name = "file"
    # file reading
    f = file_reader(file_name)

    # file lines counter
    print("Total number of lines:", file_lines_calculator(f))
    f.close()
    # words counter
    f = file_reader(file_name)
    print("Total numbers of words:", words_counter(f))
    f.close()

    # largest word counter
    f = file_reader(file_name)
    print("Largest word in a file:", largest_word_counter(f))
    f.close()

    # smallest word finder
    f = file_reader(file_name)
    print("Smallest word in a file:", smallest_word_counter(f))
    f.close()

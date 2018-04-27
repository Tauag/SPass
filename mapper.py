import pickle


def update_word_map(path='EFF_word_list.txt'):
    """
    Generates a new word_map.pickle based on the file provided
    :param path: Path to text file with new words. Should have a 5 dice key and be separated by tab
    """
    with open(path, 'r') as file_obj:
        word_map = {int(line.split('\t')[0]): 
                    line.split('\t')[1].replace('\n', '') for line in file_obj}

    with open('object/word_map.pickle', 'wb') as output:
        pickle.dump(word_map, output, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    update_word_map()

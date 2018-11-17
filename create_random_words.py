def create_words(old_file, new_file):
    '''\
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text
    after the name before appending the line to the output file.
    '''

    size = 0
    new_words = []
    with open(old_file, 'r') as read_file:
        for line in read_file:
            word = read_file.readline()
            if len(word) > 5: new_words.append(word)
        size = len(new_words)

    # import ipdb; ipdb.set_trace()

    with open(new_file, 'w', encoding='utf-8') as write_file:
        size_var_name = "const int size = " + str(size) + ";\n"
        write_file.write(size_var_name)
        words_list_name = "char *words_list[" + str(size) + "] = {\n"
        write_file.write(words_list_name)

        for w in new_words:
            write_file.write("  " + '"{}"'.format(w.rstrip()) + ",\n")

        write_file.write("};\n")


if __name__ == '__main__':
    create_words("hangman_words.txt", "random_words.dat")
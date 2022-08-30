def write_to_file(array, file_name):
    with open(file_name, 'w') as f:
        for i in array:
            f.write(i + '\n')
    f.close()
    return True
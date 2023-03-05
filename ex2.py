import os


def find_deep_files(directory):
    deep_files = []
    for file in os.listdir(directory):
        if file.startswith('deep'):
            deep_files.append(os.path.join(directory, file))
    return deep_files

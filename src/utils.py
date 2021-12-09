import os
import wfdb


def load_dat_file(path):
    signals, fields = wfdb.rdsamp(path)
    comments = fields['comments']
    return signals, fields, comments


def get_filenames_set(directory_path):
    filenames = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.dat'):
            filenames.append(filename[:-4])
    return filenames


def load_load_dat_files_from_directory(directory_path):
    dat_files = []
    for filename in get_filenames_set(directory_path):
        signals, fields, comments = load_dat_file(directory_path + filename)
        dat_files.append((signals, fields, comments))
    return dat_files

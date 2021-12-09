from utils import load_dat_file, get_filenames_set, load_load_dat_files_from_directory
from pprint import pprint
import os


current_working_dir = os.path.join(os.path.dirname(__file__))
training_data_dir_path = '/'.join(current_working_dir.split('/')[:-1]) + '/input_data/wfdb/training_I/'
filenames = get_filenames_set(training_data_dir_path)
data = load_load_dat_files_from_directory(training_data_dir_path)

filename = list(filenames)[0]
signal, fields, comments = load_dat_file(training_data_dir_path + filename)
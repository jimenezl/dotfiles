from subprocess import call

import sys
import os


def main():
    DOTFILES_DIR = os.path.dirname(os.path.abspath(__file__))

    dot_config = DOTFILES_DIR + "/../.config"

    list_of_configs_file = open(
        DOTFILES_DIR + '/config/list_of_configs.txt', 'r')

    list_of_configs = []

    for line in list_of_configs_file:
        list_of_configs.append(line.strip())

    for program_name in list_of_configs:
        call(
            ["rsync", "-r", dot_config + "/" + program_name, DOTFILES_DIR + "/config"])


    home_dir_configs_file = open(
        DOTFILES_DIR + '/home_dir/home_dir_configs.txt', 'r')

    home_dir_configs = []

    for line in home_dir_configs_file:
        home_dir_configs.append(line.strip())

    for file_name in home_dir_configs:
        call(
            ["rsync", "-r", DOTFILES_DIR + "/../" + file_name, DOTFILES_DIR + "/home_dir"])

if __name__ == '__main__':
    main()

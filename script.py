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

    print DOTFILES_DIR + "/config"
    for program_name in list_of_configs:
        print "rsync " + dot_config + "/" + program_name + " " + DOTFILES_DIR + "/config"
        call(
            ["rsync", "-r", dot_config + "/" + program_name, DOTFILES_DIR + "/config"])

if __name__ == '__main__':
    main()

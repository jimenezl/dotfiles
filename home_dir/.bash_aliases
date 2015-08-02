#!/bin/bash

alias please=sudo

alias opencv="~/.compile_opencv.sh"
alias android="~/Downloads/android-studio/bin/studio.sh"
alias c="clear"

#make sublime text have a darker ui
alias sublimedark="~/.config/sublime-text-3/Packages/User/set_sublime_ui_dark.sh"

#make sublime text have a more white ui
alias sublimelight="~/.config/sublime-text-3/Packages/User/set_sublime_ui_light.sh"

#Grep in all files in directory
alias grepfiles="grep -rnw '.' -e"

cd_and_ls() { cd ${1}; ls .; }
alias cx=cd_and_ls

#list all, even hidden, and human-readable
alias lsa='ls -lah'

#pynado downloader
alias pynado='python ~/Code/python/click/pyCoinado/venv/src/pynado.py'

#edit aliases in vim
alias aliasedit='vim ~/.bash_aliases'

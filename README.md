# dotfiles
dotfiles used by my personal machine

Simply rsyncs everything around.

#### There is no guarantee this will work on your machine

If you want to use this, change the text file in `/config` to reflect
what you want backed up from your .config directory. If you don't
want anything there backed up, make it empty. If there is anything in
your home directory you want backed up, put it in the text file in
`/home_dir` . Ie: I have my .bashrc in my home directory.

Right now this script only works if it is cloned to a directory in
your home. In the future I'll update it so it can run anywhere.

To use, go into the repo, and run:
```
python script.py
```

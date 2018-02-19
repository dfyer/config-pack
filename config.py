#!/usr/bin/env python3
from __future__ import print_function

import os


# Handler
def ask(question):
  return True
  while True:
    #answer = raw_input(question + " (y/n): ")
    return True if answer.lower() == 'y' else False

if __name__ == '__main__':
  path = "files/"

  # BASH
  if ask("Copy configs for bash?"):
    bash_path = path
    if ask("Are you using Mac OS X?"):
      bash_path += "bashrc.macosx"
    else:
      bash_path += "bashrc.linux"

      if os.path.exists('~/.bashrc'):
        with open('~/.bashrc', 'at') as dest:
          with open(bash_path, 'rt') as source:
            for line in source:
              dest.write(line)
      else:
        os.system("cp " + bash_path + " ~/.bashrc")
        print("...Complete")

  # SCREEEN
  if ask("Copy configs for screen?"):
    os.system("cp " + path + "screenrc ~/.screenrc")
    print("...Complete")

  # VIM
  if ask("Copy configs for vim?"):
    os.system("cp " + path + "vimrc ~/.vimrc")
    os.system("cp " + path + "pylint.rc ~/.pylint.rc")
    print("...Complete")

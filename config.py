import os

path = "files/"

# HYPERTERM
flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Copy configs for hyperterm? (y/n): ")

if flag is "y":
    os.system("cp " + path + "hyperterm.js ~/.hyperterm.js")
    print "Copying .hyperterm.j ...Complete"

# BASH
flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Copy configs for bash? (y/n): ")

if flag is "y":
    flag = ''
    while (flag is not 'y') and (flag is not 'n'):
        flag = raw_input("Are you using Mac OS X? (y/n): ")

    if flag is "y":
        print "Mac OS X"
        os.system("cp " + path + "bashrc.macosx ~/.bashrc")
    elif flag == 'n':
        print "LINUX"
        os.system("cp " + path + "bashrc.linux ~/.bashrc")
    print "Copying .bashrc ...Complete"

    os.system("cp " + path + "bash_profile ~/.bash_profile")
    print "Copying .bash_profile ...Complete"

# SCREEEN
flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Copy configs for screen? (y/n): ")

if flag is "y":
    os.system("cp " + path + "screenrc ~/.screenrc")
    print "Copying .screenrc ...Complete"

# VIM
flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Copy configs for vim? (y/n): ")

if flag is "y":
    os.system("cp " + path + "vimrc ~/.vimrc")
    os.system("cp " + path + "pylint.rc ~/.pylint.rc")
    print "Copying .vimrc ...Complete"

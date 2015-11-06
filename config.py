import os

#if __name__ is '__main__':
flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Copy configs for bash? (y/n): ")

if flag is "y":
    flag = ''
    while (flag is not 'y') and (flag is not 'n'):
        flag = raw_input("Are you using Mac OS X? (y/n): ")

    if flag is "y":
        print "Mac OS X"
        os.system("cp bashrc.macosx ~/.bashrc")
    elif flag == 'n':
        print "LINUX"
        os.system("cp bashrc.linux ~/.bashrc")
    print "Copying .bashrc ...Complete"

    os.system("cp bash_profile ~/.bash_profile")
    print "Copying .bash_profile ...Complete"

    os.system("source ~/.bashrc")
    print "Sourced ~/.bashrc"

flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Copy configs for screen? (y/n): ")

if flag is "y":
    os.system("cp screenrc ~/.screenrc")
    print "Copying .screenrc ...Complete"

flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Copy configs for vim? (y/n): ")

if flag is "y":
    os.system("cp vimrc ~/.vimrc")
    print "Copying .vimrc ...Complete"

flag = ''
while (flag is not 'y') and (flag is not 'n'):
    flag = raw_input("Configure git for me? (y/n): ")

if flag is "y":
    os.system("git config --global color.ui true")
    print "git config --global color.ui true"
    name = ''
    name = raw_input("Type your name: ")
    os.system("git config --global user.name \"" + name + "\"")
    print "git config --global user.name \"" + name + "\""
    addr = ''
    addr = raw_input("Type your email address: ")
    os.system("git config --global user.email " + addr)
    print "git config --global user.email " + addr

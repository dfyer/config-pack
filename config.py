import os

#if __name__ is '__main__':
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

os.system("cp screenrc ~/.screenrc")
print "Copying .screenrc ...Complete"

os.system("cp vimrc ~/.vimrc")
print "Copying .vimrc ...Complete"

os.system("git config --global color.ui true")
print "git config --global color.ui true"

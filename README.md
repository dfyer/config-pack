# Configuration Pack v0.9.1

Python 2.7 required. If you are using Python version 3.0 or above, use py3config.py 
1. Copy the configuration files
(.bashrc, .bash__profile, .screenrc, .vimrc)

> $ python config.py

2. Setup Vundle

> $ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

3. Open Vim, run :PluginInstall

4. For vim-gitgutter, run below

> cd /tmp && git clone git://github.com/airblade/vim-gitgutter.git
or
> git clone git://github.com/airblade/vim-gitgutter.git
> cp -r vim-gitgutter/* ~/.vim/

### Additional Configuration

For Mac OS X Basic Terminal,

> $ . Smyck.terminal

set hlsearch
set number
set ruler
set title
set ai
set laststatus=2

set nocompatible
set ic
set lbr

if has("syntax")
  syntax on
endif

set statusline=%F\ %m%h%r%=\ format=%{&ff},%{&fenc}\ syn=%Y\ [%l,%v]\ [%p%%\ of\ %L]

filetype indent on


set nocompatible                " be iMproved, required
filetype on                     " required
filetype off                    " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Plugin List

" a Git wrapper so awesome, it should be illegal
Plugin 'tpope/vim-fugitive'
" :A to switch header/source
Plugin 'a.vim'
" :FixWhitespace
Plugin 'bronson/vim-trailing-whitespace'
" Vim plugin for the_silver_searcher, 'ag'
Plugin 'rking/ag.vim'
" Syntax checker
Plugin 'scrooloose/syntastic'
" Javascript support
Plugin 'pangloss/vim-javascript'
" Scala support
Plugin 'derekwyatt/vim-scala'

" All of your Plugins must be added before the following line
call vundle#end()               " required
filetype plugin indent on       " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just
" :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line


" for vim-airine
" set laststatus=2
" set ttimeoutlen=50
" set t_Co=256
" alias for FixWhitespace
:command F FixWhitespace
" for syntastic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_cpp_checkers = ['cpplint']
let g:syntastic_cpp_cpplint_exec = '~/NextDB/util/cpplint.py'
:command S SyntasticToggleMode

" Tabs, indent
set shiftwidth=4
set tabstop=4
set softtabstop=4
set smarttab expandtab
set autoindent smartindent
autocmd Filetype javascript,xml,html setlocal ts=2 sts=2 sw=2
" UI
set number ruler showmode
set cursorline          " highlight current line
set scrolloff=1         " keep at least 1 lines above/below
set wildmenu            " visual autocomplete for command menu
set lazyredraw          " redraw only when we need to.
set showmatch           " highlight matching [{()}]
" searching
"set incsearch           " search as characters are entered
set hlsearch            " highlight matches
set ignorecase smartcase " case-sensitive search only for UpperCASE
set magic               " Allows pattern matching with special characters.
" folding
set foldenable
set foldlevelstart=10   " open most folds by default
set foldnestmax=10      " 10 nested fold max
set foldmethod=marker
" moving
" move to beginning/end of line
nnoremap B ^
nnoremap E $
" " $/^ doesn't do anything
nnoremap $ <nop>
nnoremap ^ <nop>
" backup
set backup
set backupdir=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set backupskip=/tmp/*,/private/tmp/*
set directory=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set writebackup

syntax enable

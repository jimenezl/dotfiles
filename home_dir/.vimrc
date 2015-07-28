call plug#begin()
Plug 'tpope/vim-sensible'
Plug 'terryma/vim-multiple-cursors'
call plug#end()

if !&scrolloff
	set scrolloff=15
endif

filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab


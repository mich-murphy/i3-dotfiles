call plug#begin("$XDG_CONFIG_HOME/nvim/plugged")
    " Catppuccin colorscheme
    Plug 'catppuccin/nvim', {'as': 'catppuccin'}
    " Handling of csv files
    Plug 'chrisbra/csv.vim'
    " Deleting of buffers without closing windows
    Plug 'moll/vim-bbye'
    " Navigation within line
    Plug 'yangmillstheory/vim-snipe'
    " Allows for editing between more targets e.g. , next (
    Plug 'wellle/targets.vim'
    " Resizing of windows
    Plug 'simeji/winresizer'
    " Cycle through yank history
    Plug 'bfredl/nvim-miniyank'
    " Fuzzy search
    Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --bin' }
    Plug 'junegunn/fzf.vim'
    " Undo tree
    Plug 'simnalamburt/vim-mundo'
    " Vim snippets
    Plug 'honza/vim-snippets'
    " LSP for Vim
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Viewing of file directory
    Plug 'preservim/nerdtree'
    " Manipulate surrounding characters e.g. quotes
    Plug 'tpope/vim-surround'
    " Read man pages in vim
    Plug 'jez/vim-superman'
    " Shortcuts for adding comments
    Plug 'tpope/vim-commentary'
    " Git integration
    Plug 'tpope/vim-fugitive'
    " Status bar
    Plug 'itchyny/lightline.vim'
    " Tmux plugins
    Plug 'christoomey/vim-tmux-navigator'
    Plug 'wellle/tmux-complete.vim'
    Plug 'tmux-plugins/vim-tmux'
    Plug 'tmux-plugins/vim-tmux-focus-events'
    " Gutter displaying changes in git
    Plug 'airblade/vim-gitgutter'
    " Add pairs to any brackets etc.
    Plug 'jiangmiao/auto-pairs'
    " Icons for NERDTree
    Plug 'ryanoasis/vim-devicons'
call plug#end()

" change resize mode key
let g:winresizer_start_key = "<leader>w"
" remove buffer error messages
set hidden
" enable paste from system clipboard
set clipboard+=unnamedplus
" relative line number
set relativenumber
set nu
" ignore case when searching without capitals
set smartcase
set ignorecase
" Highlight regex substitution
set inccommand=nosplit
" no swap file
set noswapfile
set nobackup
" remove word wrapping
set nowrap
" save undofile
set undofile
set undodir=$HOME/.config/nvim/undo
set undolevels=10000
set undoreload=10000
" use 4 spaces instead of tab & copy indent from current line
set autoindent
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
" remove -- insert -- in place of statusline
set noshowmode
" move window when specified lines from bottom
set scrolloff=8
" allow for incremental search
set incsearch
" remove highlighting after search complete
set nohlsearch

" Keyboard mappings
nnoremap <space> <nop>
let mapleader = "\<space>"

nnoremap <leader>bn :bn<cr>
nnoremap <leader>bp :bp<cr>
nnoremap <leader>bc :Bdelete<cr>
nnoremap <leader>tn gt
nnoremap <leader>tp gT
nnoremap <leader>tc :tabc<cr>
nnoremap <leader>tn :tabe<cr>
nnoremap <leader>g :split<cr>
nnoremap <leader>v :vsplit<cr>
" Mundo plugin
nnoremap <leader>u :MundoToggle<cr>
" NERDTree plugin
nnoremap <leader>f :NERDTreeToggle<cr>
" Fzf plugin
nnoremap <leader>/ :History<cr>
nnoremap <leader>/f :Files /home/mm/<cr>
nnoremap <leader>/r :Rg<cr>
nnoremap <leader>bo :Buffers<cr>
" Snipe plugin
map <leader><leader>f <Plug>(snipe-f)
map <leader><leader>ge <Plug>(snipe-ge)
nmap <leader><leader>] <Plug>(snipe-f-xp)
nmap <leader><leader>[ <Plug>(snipe-F-xp)
nmap <leader><leader>x <Plug>(snipe-f-x)
nmap <leader><leader>X <Plug>(snipe-F-x)
nmap <leader><leader>r <Plug>(snipe-f-r)
nmap <leader><leader>R <Plug>(snipe-F-r)
nmap <leader><leader>a <Plug>(snipe-f-a)
nmap <leader><leader>A <Plug>(snipe-F-a)
" Miniyank plugin
map p <Plug>(miniyank-autoput)
map P <Plug>(miniyank-autoPut)
map <leader>p <Plug>(miniyank-startput)
map <leader>P <Plug>(miniyank-startPut)
map <leader>n <Plug>(miniyank-cycle)
map <leader>N <Plug>(miniyank-cycleback)
" Yank from cursor to end of line
nnoremap Y y$
" Center cursor movement with search and line concat
nnoremap n nzzzv
nnoremap N Nzzzv
nnoremap J mzJ`z
" Set undo points when typing below characters
inoremap , ,<c-g>u
inoremap . .<c-g>u
inoremap ! !<c-g>u
inoremap ? ?<c-g>u
" Jumplist mutations
nnoremap <expr> j (v:count > 5 ? "m'" . v:count : "") . 'j'
nnoremap <expr> k (v:count > 5 ? "m'" . v:count : "") . 'k'
" Move lines
vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv

" Config for chrisbra/csv.vim
augroup filtetype_csv
    autocmd!

    autocmd BufRead,BufWritePost *.csv :%ArrangeColumn!
    autocmd BufWritePre *.csv :%UnArrangeColumn
augroup END

" Catppuccin colorscheme
colorscheme catppuccin

" Status line colorscheme
let g:lightline = {
      \ 'colorscheme': 'ayu_mirage',
      \ }

" NERDTree
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
" Close the tab if NERDTree is the only window remaining in it.
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
" If another buffer tries to replace NERDTree, put it in the other window, and bring back NERDTree.
autocmd BufEnter * if bufname('#') =~ 'NERD_tree_\d\+' && bufname('%') !~ 'NERD_tree_\d\+' && winnr('$') > 1 |
    \ let buf=bufnr() | buffer# | execute "normal! \<C-W>w" | execute 'buffer'.buf | endif

" coc.vim
let g:coc_global_extensions = [
            \ 'coc-snippets',
            \ 'coc-css', 
            \ 'coc-html',
            \ 'coc-json',
            \ 'coc-python',
            \]

" TextEdit might fail if hidden is not set.
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
if has("patch-8.1.1564")
    " Recently vim can merge signcolumn and number column into one
    set signcolumn=number
else
    set signcolumn=yes
endif

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
            \ pumvisible() ? "\<C-n>" :
            \ <SID>check_back_space() ? "\<TAB>" :
            \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
    let col = col('.') - 1
    return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
if has('nvim')
    inoremap <silent><expr> <c-space> coc#refresh()
else
    inoremap <silent><expr> <c-@> coc#refresh()
endif

" Make <CR> auto-select the first completion item and notify coc.nvim to
" format on enter, <cr> could be remapped by other vim plugin
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
            \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

vim.cmd [[
try
  if has('termguicolors')
    set termguicolors
  endif

  let g:sonokai_style = 'shusia'
  colorscheme sonokai
catch /^Vim\%((\a\+)\)\=:E185/
  colorscheme default
  set background=dark
endtry
]]

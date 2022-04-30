vim.cmd [[
try
  let g:edge_style = 'neon'
  colorscheme edge
catch /^Vim\%((\a\+)\)\=:E185/
  colorscheme default
  set background=dark
endtry
]]

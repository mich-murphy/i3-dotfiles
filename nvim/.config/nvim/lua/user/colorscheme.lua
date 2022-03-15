vim.cmd [[
try
  let g:edge_style = 'neon'
  colorscheme edge
  let g:Hexokinase_highlighters = ['virtual']
catch /^Vim\%((\a\+)\)\=:E185/
  colorscheme default
  set background=dark
endtry
]]

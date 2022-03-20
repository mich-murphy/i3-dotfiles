xrdb -merge ~/.config/X11/.Xresources
~/.fehbg &
udiskie &
setxkbmap us -variant colemak_dh
setxkbmap -option "caps:ctrl_modifier";xcape -e "Caps_Lock=Escape"&

xset +fp ~/.local/share/fonts
exec i3

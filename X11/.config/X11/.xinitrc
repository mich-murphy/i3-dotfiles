xrdb -merge ~/.config/X11/.Xresources
~/.fehbg &
exec i3
udiskie &
setxkbmap -option "caps:ctrl_modifier";xcape -e "Caps_Lock=Escape"&

xset +fp ~/.local/share/fonts

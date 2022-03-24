xrdb -merge ~/.config/X11/.Xresources
~/.fehbg &
udiskie &
pulseaudio &
setxkbmap -option "caps:ctrl_modifier";xcape -e "Caps_Lock=Escape"&

xset +fp ~/.local/share/fonts
exec i3

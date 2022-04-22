if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

xrdb -merge ~/.config/X11/.Xresources

# reset wallpaper
~/.fehbg &
# auto mount drives
udiskie &
# start audio
pipewire &
# remap caps lock
setxkbmap -option "caps:ctrl_modifier";xcape -e "Caps_Lock=Escape"&

xset +fp ~/.local/share/fonts
exec i3

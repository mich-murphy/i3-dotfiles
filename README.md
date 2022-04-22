# Dotfiles
Here are my setup files for my Arch install using i3 gaps. This is currently being used for a laptop, whicm explains some scripts and polybar modules. 

## Info
- OS: Arch
- WM: i3 gaps
- Terminal: [kitty](https://sw.kovidgoyal.net/kitty/)
- Shell: Zsh
- Browser: [Brave](https://brave.com/linux/)
- Editor: Neovim
- System monitor: [Btop](https://github.com/aristocratos/btop)
- Launcher: [Rofi](https://github.com/davatorium/rofi)
- Bar: [Polybar](https://github.com/polybar/polybar)
- Fonts: [MonoLisa](https://www.monolisa.dev/)
- Music: [Spotify-tui & Spotifyd](https://github.com/Rigellute/spotify-tui)
- GTK: [ANT Dracula](https://github.com/dracula/gtk)
- File Manager: [Ranger](https://github.com/ranger/ranger)
- Fetch: [rxfetch](https://github.com/Mangeshrex/rxfetch)
- Notifications: [Dunst](https://github.com/dunst-project/dunst)
- Compositor: [picom](https://github.com/yshui/picom)
- Colorscheme: [Edge](https://github.com/sainnhe/edge)

## Screenshots
![nvim, spotify-tui and cava screenshot](https://github.com/mrhackendbacker/Hackfiles/blob/master/wallpapers/Pictures/screenshots/2022-03-17-21:38:58-screenshot.png)
![btop, kitty and ranger screenshot](https://github.com/mrhackendbacker/Hackfiles/blob/master/wallpapers/Pictures/screenshots/2022-03-17-21:38:31-screenshot.png)

## Ansible Install
Complete ansible install can be found at [this repo](https://github.com/mich-murphy/ansible)

Following install spotifyd config must be completed:
1. create ~/.config/spotifyd/pass.txt (will look to use ansible vault in future)
2. enable systemd service
```
sudo systemctl --user enable spotifyd.service
sudo systemctl --user start spotifyd.service
```

## Installing
Requirements:
- `git`
- `stow`

Clone repository
```
git clone https://github.com/mrhackendbacker/.dotfiles.git ~
```

Run `stow` to symlink all folders (ignoring README.md etc.)
```
stow */
```
Or `stow` individual folders e.g.
```
stow nvim
```

List of installed packages can be found [here in the repo](https://github.com/mrhackendbacker/Hackfiles/blob/master/packages/.pacman.list)

## Neovim
Config was mostly taken from [this repo](https://github.com/LunarVim/Neovim-from-scratch#get-healthy), with some tweaks to plugins and keybindings.

Open nvim and enter the following:
```
:checkhealth
```

You'll probably notice you don't have support for copy/paste, also that python and node haven't been setup

First we'll fix copy/paste
```
sudo pacman -S xsel
```

Next we need to install python support (node is optional)

- Neovim python support
```
pip install pynvim
```

- Neovim node support
```
npm i -g neovim
```

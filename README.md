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

## Installing
Requirements:
- `git`
- `stow`

Clone repository
```
git clone https://github.com/mrhackendbacker/Hackfiles.git ~
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

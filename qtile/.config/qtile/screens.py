import os
from libqtile import bar, widget, qtile
from libqtile.config import Screen

colors = {
    "background": '#181818',
    "current_line": '#282828',
    "foreground": '#f8f8f2',
    "comment": '#535453',
    "black":   '#181818',
    "red":     '#ab4642',
    "green":   '#a1b56c',
    "yellow":  '#f7ca88',
    "blue":    '#7cafc2',
    "magenta": '#ba8baf',
    "cyan":    '#86c1b9',
    "white":   '#d8d8d8',
}

xf = "MonoLisa Nerd Font"
xx = 14

decor = {
    "background": colors['background'],
    "borderwidth": 3,
    "padding": 5,
    "highlight_method": 'text',
    "rounded": "true",
    "disable_drag": True,
    "inactive": colors['comment'],
    "active": colors['white'],
    "highlight_color": colors['background'],
    "this_current_screen_border": colors['red'],
    "block_highlight_text_color": colors['red'],
}

screens = [
    Screen(
        wallpaper="/home/mm/Pictures/wallpapers/delorean.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Sep(
                       linewidth=0,
                       padding=5,
                       foreground=colors['background'],
                       background=colors['background']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.GroupBox(
                    **decor,
                    font=xf,
                    fontsize=xx
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['current_line'],
                    background=colors['current_line']
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    **decor,
                    scale=0.4,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['current_line'],
                    background=colors['current_line']
                ),
                widget.WindowName(
                    padding=5,
                    font=xf,
                    fontsize=xx,
                    background=colors['current_line'],
                    foreground=colors['foreground'],
                    empty_group_string="Desktop",
                    max_chars=130,
                ),
                widget.TextBox(
                    text='\uE0B2',
                    background=colors['current_line'],
                    foreground=colors['current_line'],
                    padding=0,
                    fontsize=25
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font=xf,
                    text='\ue0dd',
                    background=colors['red'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=xx
                ),
                widget.CheckUpdates(
                    font=xf,
                    fontsize=xx,
                    update_interval=1800,
                    distro="Arch",
                    display_format="{updates}",
                    no_update_string='0',
                    foreground=colors['background'],
                    colour_have_updates=colors['green'],
                    colour_no_updates=colors['background'],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        'kitty -e sudo pacman -Syu')},
                    padding=5,
                    background=colors['white']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font=xf,
                    text='',
                    background=colors['yellow'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=xx
                ),
                widget.Memory(
                    font=xf,
                    fontsize=xx,
                    foreground=colors['background'],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        "kitty -e btop")},
                    fmt='{}',
                    padding=5,
                    background=colors['white']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font=xf,
                    text='CPU:',
                    background=colors['blue'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=xx
                ),
                widget.CPU(
                    font=xf,
                    fontsize=xx,
                    foreground=colors['background'],
                    background=colors['white'],
                    format='{freq_current}GHz {load_percent}%',
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.TextBox(
                    font=xf,
                    text='CLOCK:',
                    background=colors['magenta'],
                    foreground=colors['background'],
                    padding=5,
                    fontsize=xx
                ),
                widget.Clock(
                    font=xf,
                    fontsize=xx,
                    foreground=colors['background'],
                    background=colors['white'],
                    format="%B %d %a %I:%M %p",
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.Systray(
                    background=colors['background'],
                    icon_size=10,
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=colors['background'],
                    background=colors['background']
                ),
            ],
            35,
            background=colors['current_line'],
        ),
    ),
]

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
from screens import screens

# Default setting and applications
mod = "mod4"
terminal = "kitty" 
browser = "brave"

# Autostart applications
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/local/bin/autostart.sh")
    subprocess.run([home])

# My functions
@lazy.function
def inc_margin(qtile):
    qtile.current_layout.margin += 10
    qtile.current_group.layout_all()

@lazy.function
def dec_margin(qtile):
    if qtile.current_layout.margin != 0:
        qtile.current_layout.margin -= 10
        qtile.current_group.layout_all()

# Keymappings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Window movement
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "space", lazy.layout.flip(), desc="Move window focus to other window"),

    # Resizing windows
    Key([mod, "control"], "h", lazy.layout.shrink(), lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow(), lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "f", lazy.window.toggle_floating(), desc="Toggle floating windows"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod], "o", lazy.layout.maximize(), desc="Toggle window to max and min size"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "equal", inc_margin(), desc="Increase window margin"),
    Key([mod], "minus", dec_margin(), desc="Decrease window margin"),

    # Launching applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch web browser"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown Qtile"),

    # Function controls
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("changevolume.sh up"), desc="Increase volume"),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("changevolume.sh down"), desc="Decrease volume"),
    Key([mod], "XF86AudioMute", lazy.spawn("changevolume.sh mute"), desc="Mute volume"),
    Key([mod], "XF86MonBrightnessUp", lazy.spawn("changebrightness.sh up"), desc="Increase brightness"),
    Key([mod], "XF86MonBrightnessDown", lazy.spawn("changebrightness.sh down"), desc="Decrease brightness"),

    # Rofi
    Key([mod], "r", lazy.spawn("rofi -modi drun,run -show drun"), desc="Rofi launch menu"),
    Key([mod, "shift"], "x", lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu"), desc="Rofi shutdown menu"),
    Key([mod], "c", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'"), desc="Rofi shutdown menu")
]

groups = [
    Group("1", label="1"),
    Group("2", label="2", 
          matches=[
              Match(wm_class=["Brave-browser"]),
              Match(wm_class=["Firefox"])
          ]),
    Group("3", label="3", 
          matches=[
              Match(wm_class=["Zathura"])
          ]),
    Group("4", label="4"),
    Group("5", label="5"),
    Group("6", label="6"),
    Group("7", label="7"),
    Group("8", label="8"),
    Group("9", label="9")
]

for i in groups:
    keys.extend(
        [
            Key( [mod], i.name, lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            Key([mod, "control"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

groups.append(ScratchPad('Scratchpad', [
    DropDown("term", "kitty",
             width=0.75, height=0.9,
             x=0.125, y=0.05, opacity=1)
]))

keys.extend([
    Key([mod, 'shift'], "v",
        lazy.group['Scratchpad'].dropdown_toggle('term'))
])

# Layout settings
layouts = [
    layout.MonadTall(
        border_focus="#d38aea",
        border_normal="#2b2d3a",
        border_width=3,
        margin=10
    ),
    layout.MonadWide(
        border_focus="#d38aea",
        border_normal="#2b2d3a",
        border_width=3,
        margin=10
    ),
    layout.MonadThreeCol(
        border_focus="#d38aea",
        border_normal="#2b2d3a",
        border_width=3,
        margin=10,
        new_client_position="after_current"
    ),
    layout.Floating(
        border_width=0
    )
]

# Widget and extension settings
# widget_defaults = dict(
#     font="MonoLisa",
#     fontsize=12,
#     padding=3,
# )

# extension_defaults = widget_defaults.copy()
extension_defaults = dict(
    font="MonoLisa Nerd Font",
    fontsize=13,
    padding=3,
)

# # Bar and screen settings
# screens = [
#     Screen(
#         wallpaper="~/Pictures/wallpapers/delorean.png",
#         wallpaper_mode="fill",
#         top=bar.Bar(
#             [
#                 widget.CurrentLayout(),
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.Chord(
#                     chords_colors={
#                         "launch": ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 widget.TextBox("my config", name="default"),
#                 widget.Battery(
#                     font="MonoLisa",
#                     background="#2b2d3a",
#                     foreground="#c5cdd9"
#                 ),
#                 widget.Systray(),
#                 widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                 widget.QuickExit(),
#             ],
#             24,
#         ),
#     ),
# ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button2", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button3", lazy.window.bring_to_front()),
]

# General settings
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

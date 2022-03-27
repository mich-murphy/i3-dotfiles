#!/usr/bin/env bash

## Install ansible
sudo pacman -S ansible git

## Pull ansible
sudo ansible-pull -U https://github.com/mich-murphy/dotfiles.git

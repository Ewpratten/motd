# motd
💬 My script for displaying information in my terminals

## Installation
This is just a script, not a full tool. To use this, just grab the `motd.py` file, and run it on any computer with `python3.7` installed. To start MOTD with your shell, add `python3 /path/to/motd.py` to your shell's RC file (I use `~/.zshrc`).

## Modify the flags
To use your own GitHub account, or override other settings, refer to the flags listed in the program help:
```
usage: motd.py [-h] [-g GITHUB_USERNAME] [-o GITHUB_ORG]

optional arguments:
  -h, --help            show this help message and exit
  -g GITHUB_USERNAME, --github-username (default Ewpratten)
  -o GITHUB_ORG,      --github-org      (default frc5024)
```

## Features
This MOTD script will give a small printout when run. This includes:
 - Current time
 - Current date
 - Number of GitHub issues

In the future, a simple weather readout may be added.

## Example
Here is an example from my laptop:
```
Welcome ewpratten!
It is currently 3:28 on Fri August 30, 2019.
You have 4 issues open on GitHub. View them here: https://lynkz.me/zsWWvEn
```
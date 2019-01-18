#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-A", "--all", action="store_true",
                    help="Install all .*rc files")
parser.add_argument("-b", "--bash", action="store_true",
                    help="Install .bashrc")
parser.add_argument("-v", "--vim", action="store_true",
                    help="Install .vimrc")
parser.add_argument("-s", "--screen", action="store_true",
                    help="Install .screenrc")
parser.add_argument("-m", "--mac", action="store_true",
                    help="Check if installing mac (only affects .bashrc path)")
parser.add_argument("--backup", action="store_true", default=True,
                    help="Create backup for existing .*rc files")
args = parser.parse_args()

SRC_BASE = "files/"

def get_bashrc():
  if args.mac:
    return SRC_BASE + "bashrc.macosx"
  else:
    return SRC_BASE + "bashrc.linux"

# Setup
targets = {}
if args.all:
  targets[os.path.expanduser("~/.bashrc")] = get_bashrc()
  targets[os.path.expanduser("~/.vimrc")] = SRC_BASE + "vimrc"
  targets[os.path.expanduser("~/.screenrc")] = SRC_BASE + "screenrc"
else:
  if args.bash:
    targets[os.path.expanduser("~/.bashrc")] = get_bashrc()
  if args.vim:
    targets[os.path.expanduser("~/.vimrc")] = SRC_BASE + "vimrc"
  if args.screen:
    targets[os.path.expanduser("~/.screenrc")] = SRC_BASE + "screenrc"
print("Targets: ")
print("\n".join(["\t" + x for x in targets.keys()]))

if targets:
# Backup
  if args.backup:
    print("Backup: ")
    for dst in targets:
      if os.path.exists(dst):
        backup_cmd = ["cp", dst, dst+".backup"]
        backup_cmd = " ".join(backup_cmd)
        print("\t" + backup_cmd, end='')
        os.exec(backup_cmd)
        print("\t..backup complete!")

# Copy
  print("Install: ")
  for dst in targets:
    install_cmd = ["cp", targets[dst], dst]
    install_cmd = " ".join(install_cmd)
    print("\t" + install_cmd, end='')
    os.exec(install_cmd)
    print("\t..install complete!")

# Student Manager Main
# Author  : C14147@github.com
#
# Copyright (c) 2024-2025 by C14147 <ffffasddd@163.com>.
# Licensed in Apache 2.0

import subprocess
import argparse
import login


__version__ = "Development Edition"

# Set Arguments for Input
parser = argparse.ArgumentParser(description="Student Manager")
parser.add_argument("-v", "--version", action="store_true", help="Show Version")
parser.add_argument("-s", "--standalone", action="store_true", help="Run in Standalone Mode")
parser.add_argument("-e", "--debug", action="store_true", help="Run in Debug Mode")
parser.add_argument("-u", "--user", action="store_true", help="Users Who Need to Login")
parser.add_argument("-d", "--database", action="store_true", help="Database Path")
args = parser.parse_args()

# Check Wheather SoftwareManagent is installed
_checker = subprocess.Popen(["SoftwareManagement","--version"])
_checker.wait()
if _checker.poll() != 0 or args.standalone:
    isStandaloneMode = True
else:
    isStandaloneMode = False
_checker.kill()
del _checker

# Show login window
if isStandaloneMode:
    login.runLogin()


# Student Manager Constents
# Author  : C14147@github.com
#
# Copyright (c) 2024-2025 by C14147 <ffffasddd@163.com>.
# Licensed in Apache 2.0
r"""
Student Manager Constents
This module creates some constents for this project.
"""
import os

NOT_DEFINED = None
EMPTY = NOT_DEFINED

MALE = "M"
FEMALE = "F"

# C14147 Remote Connection Toolkit Whether Available
RCT_AVAILABLE = False

# Login Background Image
LOGIN_BGI = True

# File Types
SQLite = "SQLite (*.db *.sqlite *.sqlite3)"

# SQL Type Looker
def sql_looker(path: str) -> str:
    if path.endswith(
        ('.db','.sqlite','.sqlite3')    # SQLite
    ):
        return 'sqlite3'


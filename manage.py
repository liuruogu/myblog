#!/usr/bin/env python
#Don't do any change on this project
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

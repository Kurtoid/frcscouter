#!/usr/bin/python3
import os
import sys

if __name__ == "__main__":
    # GETTING-STARTED: change 'myproject' to your project name:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scouter.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

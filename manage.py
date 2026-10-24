#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bihar_b2b_tours.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Check that it is installed and available in your environment."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

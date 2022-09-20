#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv
import pathlib

def main():
    """Run administrative tasks."""
    # DOT_ENV_PATH = pathlib.Path() / '.env' #Checking Dotenv file path stored somewhere to see if it exist
    # if DOT_ENV_PATH.exists():
    #     dotenv.read_dotenv()   
    # else:
    #     print('No .env file found, be sure to add it!')
    
    dotenv.read_dotenv()    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

import sys
import os
from .options import get_options
from .find import is_env, find_env
from .utility import error

def main():
    options = get_options(sys.argv[1:])
    if options.env:
        if is_env(options.env):
            print(options.env)
        else:
            error('{:s} is not a virtualenv'.format(options.env))
    else:
        env = find_env(os.getcwd())
        if env:
            print(env)
        else:
            error('no virtualenv found')

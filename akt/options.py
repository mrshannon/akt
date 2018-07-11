import argparse


def make_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        usage='akt [-h] [-e ENV] COMMAND ...',
        description="""Run a command inside a virtualenv.
    
akt will look in the current and all parent directories for the
virtualenv to use.  Place a .aktrc file with the path to a virtualenv in
the current or a parent direcotry or use the '-e' flag to specify a
virtualenv.""")
    parser.add_argument(
        '-e', '--env', help='path to the virtualenv to use')
    parser.add_argument(
        'command', nargs='*',
        help='command to run, defaults to the current shell')
    return parser


def get_options(argv):
    parser = make_parser()
    return parser.parse_args(argv)

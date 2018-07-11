import os


def expand_path(path):
    return os.path.realpath(os.path.expandvars(path))


def is_env(path):
    activate = os.path.join(path, 'bin', 'activate')
    if os.path.exists(activate):
        with open(activate) as infile:
            return 'export VIRTUAL_ENV' in infile.read()
    return False


def paths(path):
    while True:
        yield path
        if os.path.dirname(path) == path:
            break
        path = os.path.dirname(path)


def read_rc(path):
    with open(path, 'r') as infile:
        for line in infile:
            yield expand_path(line.rstrip())


def traverse(path):
    for path in paths(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path, name)
            if os.path.isfile(fullpath) and name == '.aktrc':
                yield from read_rc(fullpath)
        for name in os.listdir(path):
            fullpath = os.path.join(path, name)
            if os.path.isdir(fullpath):
                yield fullpath
        

def find_env(path):
    for path in traverse(path):
        if is_env(path):
            return path

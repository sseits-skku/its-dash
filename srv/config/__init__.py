import os.path
from yaml import load, dump, CLoader as Loader

env = 'development'
env += '.yaml'
cur_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(cur_path, env), 'r') as e:
    conf = e.read()

CONFIG = load(conf, Loader=Loader)

__all__ = [ 'CONFIG' ]

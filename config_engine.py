import os
from os import path

CONFIG = '.lime-config'

def searchdirs():
  yield os.environ.get('HOME')

  parents=''
  for dir in os.getcwd().split('/'):
    parents += '/' + dir
    yield parents
    
def decomment(line):
  return line[:line.find('#')]

def key_value_split(line):
  if ':' in line:
     return [field.strip() for field in line.split(':', 1)]
  else:
    words = line.split()
    if len(words) == 2 and words[1] == 'unset':
      return [words[0], None]

possible_configfiles = [path.join(dir, CONFIG) for dir in searchdirs()]
configfiles = [file for file in possible_configfiles if path.isfile(file)]

lines = [line for file in configfiles for line in open(file)]
key_value_pairs = [key_value_split(decomment(line).strip()) for line in lines]
config = dict(kv for kv in key_value_pairs if kv)


if __name__ == '__main__':
  
  from sys import argv, stdout, stderr, exit

  if len(argv) > 1:
    
    if argv[1] == 'listfiles':
      stdout.write(' '.join(configfiles) + '\n')
    elif argv[1] in ('make', 'shell'):
      for k, v in config.items():
        if v is not None:
          stdout.write('export %s=%s\n' % (k,v))
        else:
          stdout.write('unexport %s\n' % k)
    else:
      stderr.write('unrecognized format argument\n')
      exit(1)
  else:
    stderr.write('missing format argument\n')
    exit(1)

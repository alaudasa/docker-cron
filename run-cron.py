#!/usr/bin/python

import os
from os import path
from subprocess import call

def empty_dir(d):
    for the_file in os.listdir(d):
        file_path = path.join(d, the_file)
        try:
            if path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e    


if __name__ == '__main__':
    empty_dir('/etc/cron.d/') 
    env_header = ''
    for env_n, env_v in os.environ.items():
        env_header = env_header + env_n + '='+ env_v + '\n'
    for cronfile in  os.listdir('/cron'):
        with open(path.join('/cron', cronfile), 'r') as fread:
            with open(path.join('/etc/cron.d/', cronfile.replace('.','_')), 'w') as fwrite:
                fwrite.write(env_header)
                fwrite.write('\n')
                fwrite.write(fread.read())
                fwrite.write('\n')
    call(['cron', '-f', '-L', '15'])
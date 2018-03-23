from celery import Celery

import subprocess

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='rpc://')

@app.task
def run(prog,args):
   process = subprocess.Popen(prog + ' ' + args.join(' '), shell=True, stdout=subprocess.PIPE)
   output, error = process.communicate()
   return output


import os
import sys
from subprocess import Popen

# run all child scripts in parallel
processes = [Popen([sys.executable, filename], cwd=dirpath)
             for dirpath, dirname , filenames in os.walk('.')
             for filename in filenames
             if filename == 'run.py']

# wait until they finish
for p in processes:
    p.wait()
print("all done")

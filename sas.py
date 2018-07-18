#
# This file is part of IsoWorlds, licensed under the MIT License (MIT).
#
# Copyright (c) Edwin Petremann <https://github.com/Isolonice/>
# Copyright (c) contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#!python3
# -*- coding: utf-8 -*-

import os
import subprocess
import threading
import time
from multiprocessing import Pool


class KThread(threading.Thread):
    def __init__(self, dirs2, dirs, j, k):
        threading.Thread.__init__(self)
        self.dirs = dirs
        self.dirs2 = dirs2
        self.j = j
        self.k = k
        self.value = True

    def run(self):
        # If already handled by IsoWorlds plugin, deleting region folder just in case (if loaded by another unlegit way)
        if "-IsoWorld@PUSHED@PULL" in (self.dirs2[self.k]):
            name = self.dirs2[self.k].split("@PUSHED@PULL")
            name = name[0]
            print("IsoWorld pull rapporter détécté: " + self.dirs2[self.k])
            cmd = 'rm -Rf /servers/' + self.dirs[self.j] + '/Isolonice/' + self.dirs2[self.k] + '/region'
	    print(cmd)
	    print(csf(cmd))
            cmd2 = 'rsync -asv matterr:/isoworlds/' + self.dirs[self.j] + '/' + name + '/region' + ' /servers/' + self.dirs[self.j] + '/Isolonice/' + self.dirs2[self.k] + '/'
            print(cmd2)
            print(csf(cmd2))
            cmd3 = 'mv /servers/' + self.dirs[self.j] + '/Isolonice/' + self.dirs2[self.k] + ' /servers/' + self.dirs[self.j] + '/Isolonice/' + name
            print(cmd3)
            print(csf(cmd3))
            cmd4 = 'stat -c %u /servers/' + self.dirs[self.j] + '/server.properties'
            print(cmd4)
            print(csf(cmd4))
            owner = os.popen(cmd4).read().split("\n")
            owner = owner[0]
            cmd5 = 'chown -R ' + owner + ':' + owner + ' /servers/' + self.dirs[self.j]
            print(cmd5)
            print(csf(cmd5))

            self.value = False
            return False
            # If already handled (pushed)
        if "-IsoWorld@PUSHED" in (self.dirs2[self.k]):
            self.value = False
            return False
        if "-IsoWorld@PUSH" in (self.dirs2[self.k]):
            # Getting real name of an IsoWorld (without tags, uuid-IsoWorld)
            name = self.dirs2[self.k].split("@PUSH")
            name = name[0]
            # Create path even if it exists
            mkdir = 'ssh matterr mkdir -p /isoworlds/' + self.dirs[self.j] + '/' + name
            print(csf(mkdir))
            print("IsoWorld à push détécté: " + self.dirs2[self.k])
            # Copy local region folder to remote server with /isoworlds/uuidSrv/uuidWorld/ path
            cmd2 = 'rsync -azv /servers/' + self.dirs[self.j] + '/Isolonice/' + self.dirs2[self.k] + '/region' + ' matterr:/isoworlds/' + self.dirs[self.j] + '/' + name + '/'
            print(cmd2)
            print(csf(cmd2))
            # Deleting local region folder
            cmd3 = 'rm -Rf /servers/' + self.dirs[self.j] + '/Isolonice/' + self.dirs2[self.k] + '/region'
            print(cmd3)
            print(csf(cmd3))
            cmd4 = 'mv /servers/' + self.dirs[self.j] + '/Isolonice/' + self.dirs2[self.k] + ' /servers/' + self.dirs[self.j] + '/Isolonice/' + name + '@PUSHED'
            print(cmd4)
            print(csf(cmd4))
            cmd5 = 'stat -c %u /servers/' + self.dirs[self.j] + '/server.properties'
            print(cmd5)
            print(csf(cmd5))
            owner = os.popen(cmd5).read().split("\n")
            owner = owner[0]
            cmd6 = 'chown -R ' + owner + ':' + owner + ' /servers/' + self.dirs[self.j]
            print(cmd6)
            print(csf(cmd6))

            self.value = False
            return False

# Shell cmd execution
def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()

# Check callback
def csf(cmd):
    try:
        subprocess_cmd(cmd)
        return "SUCCESS: " + cmd
    except ValueError:
        return "FAILED: " + cmd

def push():
    # Getting every server folders splitted by line returns
	cmd = 'ls /servers/'
    dirs = os.popen(cmd).read().split("\n")

    # Getting every IsoWorlds folder for each server folders
    for j in range(len(dirs)):
        if dirs[j][:3] == "aremettredev" or dirs[j][:3] == "" or dirs[j][:3] == "OLD":
            continue
        cmd1 = 'ls /servers/' + dirs[j] + '/Isolonice'
        dirs2 = os.popen(cmd1).read().split("\n")

        for k in range(len(dirs2)):
            # Init thead
            thread = KThread(dirs2, dirs, j, k)
            # Starting thread
            thread.start()
            # Waiting end of thread
            thread.join()
            if not thread.value:
                continue


print("Fin")

# Init with 5 pool
if __name__ == "__main__":
    check = True
    pool = Pool(5)
    while check:
        # globals()[sys.argv[1]]()
        start_time = time.time()
        push()
        print("--- %s secondes ---" % (time.time() - start_time))
        time.sleep(5)

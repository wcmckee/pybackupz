# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os

# <codecell>

import os.path

# <codecell>

cd /home/will/Documents/photoz

# <codecell>

class Backup(object):
    def findfiles(self, filestring):
        filecur = os.listdir(os.curdir)
        for filename in filecur:
            if filestring in filename:
                yield filename
            

# <codecell>

"as" in "Texas"

# <codecell>

if 'as' in 'texas':
    print 'yes as is in texas'

# <codecell>

app = Backup()

# <codecell>

app.findfiles('mp4')

# <codecell>

for fileza in app.findfiles('last'):
    print fileza

# <codecell>

import time

# <codecell>



from PIL import Image
from PIL import ImageDraw
from PIL import ImageChops
import random
import os
from PIL import ImageEnhance
from ftplib import FTP


# <codecell>

os.listdir

# <codecell>

ftp = FTP('ftp.freshfigure.com')
ftp.login('ipython', 'Testing123now#')

# <codecell>

import shutil
import time
import PIL

# <codecell>

copyFilez = shutil.copy2('/home/will/Documents/photoz/lastsnap.jpg', '/home/will/Downloads/photoz/lastsnap.jpg')

# <codecell>

'''
for x in range(0, 3):
    time.sleep(20)
    copyFilez
    print('done!')

'''

# <codecell>

savImz = PIL.Image.open(fileza)

# <codecell>

savImz.show()

# <codecell>



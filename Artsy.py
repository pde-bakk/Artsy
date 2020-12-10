#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    Artsy.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: peerdb <peerdb@student.codam.nl>             +#+                      #
#                                                    +#+                       #
#    Created: 2020/11/30 19:16:01 by peerdb        #+#    #+#                  #
#    Updated: 2020/11/30 19:52:56 by peerdb        ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import random
import sys
import time

from PIL import Image

from GenerateASCII import generate_ascii

if len(sys.argv) >= 2:
    if sys.argv[1] == "flex":
        im = Image.open("imgs/flex.gif")
    elif sys.argv[1] == "homie":
        if random.randint(0, 4) == 1:
            im = Image.open("imgs/christmashomie.gif")
        else:
            im = Image.open("imgs/kissahomie.gif")
    else:
        im = Image.open("imgs/monkaSTEER.gif")
else:
    im = Image.open("imgs/thor.gif")

print(im.n_frames)

while True:
    for frame in range(im.n_frames):
        im.seek(frame)
        generate_ascii(im)
        time.sleep(4.0 / im.n_frames)

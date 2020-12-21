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

import sys, time, random, os
from PIL import Image

from GenerateASCII import generate_ascii

if len(sys.argv) >= 2:
	imageName = sys.argv[1] + ".gif"
else:
	imageName = "thor.gif"

im = Image.open("imgs/" + imageName)
# print(im.n_frames)

while True:
    for frame in range(im.n_frames):
        im.seek(frame)
        generate_ascii(im)
        time.sleep(4.0 / im.n_frames)
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
from GenerateASCII import GenerateASCII

if len(sys.argv) >= 2:
	arg =  sys.argv[1]
	if arg == "flex":
		imageName = "flex.gif"
	elif arg == "homie":
		if random.randint(0, 4) == 1:
			imageName = "christmashomie.gif"
		else:
			imageName = "kissahomie.gif"
	elif arg == "melt":
		imageName = "melt.gif"
	elif arg == "tunnel":
		imageName = "tunnel.gif"
	elif arg == "dancing":
		imageName = "dancing.gif"
	elif arg == "codywave":
		imageName = "codywave.gif"
	else:
		imageName = "monkaSTEER.gif"
else:
	imageName = "monkaSTEER.gif"

im = Image.open("imgs/" + imageName)
# print(im.n_frames)

while True:
	for frame in range(im.n_frames):
		im.seek(frame)
		GenerateASCII(im)
		time.sleep( 2.5 / im.n_frames )
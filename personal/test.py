import sys
from PIL import Image

images = []

for args in sys.agrv[1:]:
	image = Image.open(args)
	images.append(image)

images[0].save("marriage.gif", save_all=True, append_images=[images[1:]], duration=300, loop=0)

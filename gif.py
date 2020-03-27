# pip install Pillow
from PIL import Image, ImageDraw
import glob
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required = True, help = "Path to the folder contaning all images")
ap.add_argument("-f", "--format", required = True, help = "Format of images, exemples: png jpg")
ap.add_argument("-n", "--name", required = False, help = "Name of the gif")
args = vars(ap.parse_args())

files = glob.glob(args["path"]+"*."+args["format"])

gif, *frames = [Image.open(f) for f in sorted(files)]

if not args["name"]:
    output_name = "gif.gif"
else:
    output_name = args["name"]+".gif"

gif.save(output_name, format='GIF', append_images=frames,save_all=True, duration=1000, loop=0)
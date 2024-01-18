#!/usr/bin/env python3

# imports required modules
import subprocess
import sys
import argparse
import ast
import os

# Checks to see if external module "Pillow" is installed on the system by attempting to import the Image module
# If pillow is not installed, installs it via a system subprocess
try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image")
parser.add_argument("-d", "--directory")
parser.add_argument("-di", "--dimensions")
parser.add_argument("-t", "--type")
parser.add_argument("-r", "--rotation")
parser.add_argument("-de", "--destination")


# args.name_of_argument will allow the passed arguments to be accessed within the program
args = parser.parse_args()
lit = ast.literal_eval
imageList = []
if args.image is not None:
    ImageFile = args.image
    # Runs a brief test to ensure file is a usable image file
    with Image.open(ImageFile) as file:
        originalFormat = file.format
    imageList.append(ImageFile)
if args.directory is not None:
    DirectoryPath = args.directory
    for item in os.listdir(DirectoryPath):
        try:
            with Image.open(item) as file:
                originalFormat = file.format
            imageList.append(item)
        except OSError:
            pass
    if imageList is None:
        raise SyntaxError("Error: Directory contains no image files.")
if args.dimensions is not None:
    ImageDimensions = lit(args.dimensions)
    if type(ImageDimensions) is not tuple:
        print("Invalid dimensions.")
        while True:
            try:
                x = int(input("Image X dimension:\n"))
                break
            except ValueError:
                print("Invalid input")
        while True:
            try:
                y = int(input("Image Y dimension:\n"))
                break
            except ValueError:
                print("Invalid input.")
        ImageDimensions = (x, y)
else:
    ImageDimensions = ()
if args.type is not None:
    FileType = args.type
else:
    FileType = ""
if args.rotation is not None:
    Rotation = lit(args.rotation)
    if type(Rotation) is not int:
        print("Invalid argument for rotation.")
        while True:
            try:
                Rotation = int(input("Image rotation in degrees:\n"))
                break
            except ValueError:
                print("Invalid input")
else:
    Rotation = 0
if args.destination is not None:
    NewDirectory = args.destination
else:
    NewDirectory = os.getcwd()


# Checks user syntax before attempting to process files
if args.image is None and args.directory is None:
    raise SyntaxError("Error: No file passed to process")
if args.dimensions is None and args.type is None and args.rotation is None:
    raise SyntaxError("Error: No arguments passed for processing")


def processor(imagefile):
    with Image.open(imagefile) as image:
        if ImageDimensions is ():
            dimensions = (image.size[0], image.size[1])
        else:
            dimensions = ImageDimensions
        f, e = os.path.splitext(imagefile)
        if FileType is "":
            filetype = e
        else:
            filetype = FileType
        outputname = "{}{}".format(os.path.basename(f), filetype)
        finalpath = os.path.join(NewDirectory, outputname)
        image.rotate(Rotation).resize(dimensions).save(finalpath)


for file in imageList:
    processor(file)

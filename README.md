This is a python program that allows either an image file or a directory of image files to be passed in the command line and have the file type, rotation, image dimensions, and file destination manipulated via arguments.
To Use:
Run the python file in your command line followed by the correlating flags.

Flag definitions:
-i
	Image file. Precedes the file location for a single image to be manipulated.
-d
	Directory. Precedes the path to a directory of images to be batch processed
-di
	Dimensions. The following input should be in the x,y format.
-t
	File type. Precedes the file path for the intended type eg. .jpg
-r
	Rotation in degrees.
-de
	Destination directory. If left blank, destination will be the current working directory.

Example:
./PhotoManip.py -i ./test_image.jpg -di 100,100 -de ~/test_directory


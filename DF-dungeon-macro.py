# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:27:02 2023

@author: French Vivec
"""
#%% Import packages
from os.path import exists
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
from writer import write_macro
import cv2

DEBUG = True

#%% Import image
progress = 0
print()
while progress!=1:
    image_name = input("Enter the filename of your dungeon map (ex: dungeon.png): ")

    if exists(image_name):
        dungeon = cv2.imread(image_name)
        progress = 1

    else:
        print('No "'+image_name+'" in root folder. Make sure your image is in the same folder as this program.\n')

#%% Remove the .png for the macro name and other
macro_name = ''
for char in image_name:
    if char!='.':
        macro_name += char
    else:
        break


#%% Put into greyscale for morphological operations
dungeon_gray = cv2.cvtColor(dungeon, cv2.COLOR_BGR2GRAY)

if DEBUG:
    plt.imshow(dungeon_gray)
    plt.savefig("./"+macro_name+"-01_gray.png")
    plt.close()

#%% Apply a binary closing to remove grid and superfluous details
# To learn about morphological closing: https://en.wikipedia.org/wiki/Closing_(morphology)
struct = ndimage.generate_binary_structure(2, 2)
dungeon_corrected = ndimage.binary_closing(dungeon_gray, struct, 2)

if DEBUG:
    plt.imshow(dungeon_corrected)
    plt.savefig("./"+macro_name+"-02_closing.png")
    plt.close()

#%% Resize the image as requested and make it a binary map (True or False instead of a grayscale)

# If image is square, ask for the new side length
square = dungeon_corrected.shape[0]==dungeon_corrected.shape[1]

if square:
    progress = 0
    print("\nMap is squared")
    while progress!=1:
        length = input("Enter the new side length: ")

        if length.isnumeric():
            height = int(length)
            width  = int(length)
            progress = 1

        else:
            print('The length must be a valid number.\n')
else:
    progress = 0
    print("\nMap is not a square.")
    while progress!=1:
        side_to_change = input("Would you rather define the height (h) or width (w) for resizing ? ")

        if side_to_change in ['h', 'w']:
            progress = 1

        else:
            print('Enter either \'h\' or \'w\'\n')
    
    progress = 0
    while progress!=1:
        length = input("\nNew height/width:")

        if length.isnumeric():
            if side_to_change == 'h':
                height = int(length)
                width = int(height*dungeon_corrected.shape[1]/dungeon_corrected.shape[0])
            else:
                width = int(length)
                height = int(width*dungeon_corrected.shape[0]/dungeon_corrected.shape[1])
            progress = 1

        else:
            print('The length must be a valid number.\n')

dungeon_resized = cv2.resize(np.float32(dungeon_corrected), dsize=(width, height), interpolation=cv2.INTER_LINEAR_EXACT)

if DEBUG:
    plt.imshow(dungeon_resized)
    plt.savefig("./"+macro_name+"-03_resized.png")
    plt.close()

#%% Resize the image as requested and make it a binary map (True or False instead of a grayscale)
dungeon_map = np.array(dungeon_resized) > 0
progress = 0
print("\nDo you want fancy junctions ?")
print("(Just a fun thing I realized: If I changed one setting on the details-removal part, some tunnel and room junctions will be curved instead of 90° angles)")
print("This could lead to artefacts, it's not tested at all. (Hail serendipity !)")
while progress!=1:
    fancy = input("(y/n):")
    if fancy=="y":
        struct = ndimage.generate_binary_structure(2, 1)
        progress = 1
    elif fancy=="n":
        struct = ndimage.generate_binary_structure(2, 2)
        progress = 1
        
dungeon_map = ndimage.binary_erosion(dungeon_map, struct, 1)

if DEBUG:
    plt.imshow(dungeon_map)
    plt.savefig("./"+macro_name+"-04_map.png")
    plt.close()
#%% Create macro
macro_name = macro_name+'-'+str(width)+'x'+str(height)
write_macro(macro_name, dungeon_map)
print("Macro successfully created as '"+macro_name+".mak'. You can now move it to 'Dwarf Fortress\prefs\macros'.")
print("Your dungeon will take a space of "+str(width)+" (width/x-axis) by "+str(height)+" (height/y-axis).")
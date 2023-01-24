# DF 5e Dungeon Converter
 A simple python script to turn dungeons from https://donjon.bin.sh/5e/dungeon/ into Dwarf Fortress macros

## Description
A really simple (understand: improvised, unoptimized, non-ergonomic) script which will turn your randomly generated DnD 5e Dungeons into a Dwarf Fotress macro.

## Instructions
I do not know how to create an executable (oh, and side-note: DO NOT RUN A RANDOM EXECUTABLE FROM THE INTERNET) or even how to store all packages imported for publication purposes, so you'll need to do a few things to run this.

1. Install python 3 from the official python website (you can find the link on the wikipedia page https://en.wikipedia.org/wiki/Python_(programming_language), a good trick to remember if you're not sure if a website if official or not).

2. Install the following packages if you don't already have them:
   'numpy',
   'scipy',
   'opencv-python'
   
   To install a python package you need to open your OS terminal or powershell window. And enter the following command: 'pip install \<package name\>'

3. Download this repository and unzip-it somewhere if you need to.

4. Generate your dungeon via https://donjon.bin.sh/5e/dungeon/. It can be any size, any options. But due to the need to resize-the image, shapes that are not squares may look weird in the final result. (Also corridor width will not always be consistent).

5. Do not generate the dungeon. Instead download the preview on the right. Give it the name you want.

6. Put the new image in the scripts folder.

7. From a terminal or powershell, navigate to the newly created folder containing the .py files.

8. Execute the following command: "python DF-dungeon-macro.py"

9. Follow the instructions
    9.a If your map is squared, you will be prompted for the side length
    9.b If your map is rectangular, you must choose a side to change its length. The other side will be modified to kep the ratio.
    9.c I noticed that modifying a setting (the structure to use for morphological operations) could lead to corridor junctions being slightly curved. This is an option if you want some fancier corridors.

10. If all worked, you will now have a .mak file in the folder. Move it to "Dwarf Fortress\prefs\macros". Steam players can find the game in "X:\Steam\steamapps\common\'

Done ! You can now use the macro to DIG your dungeon. It won't work with walls. 

Now, as I said this is not optimized and does not render the generated dungeon perfectly. The code is open. Feel free to modify it and make suggestions. If have included two maps and their resulting macros in the repository.

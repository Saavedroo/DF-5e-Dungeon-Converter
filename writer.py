# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:47:18 2023

@author: Léo M
"""

def write_macro(name, dig_map):
    import numpy as np
    
    if type(name) != str:
        print("Enter a valid macro name")
        return 2
    
    fb_char = ["\\","/",":","*","?","\"","<",">","|"]
    for char in name:
        if char in fb_char:
            print("Filename cannot contain characters", fb_char)
            return 2
    with open(name+".mak", "w") as f:
        f.write(name+"\n")
        i=0
        x = dig_map.shape[1]
        while i < dig_map.shape[0]:
            if i%2==0:
                for j in range(dig_map.shape[1]):
                    if dig_map[i, j]:
                        f.write("		SELECT\n")
                        f.write("	End of group\n")
                        f.write("		SELECT\n")
                        f.write("	End of group\n")
                    if j<dig_map.shape[1]-1:
                        f.write("		KEYBOARD_CURSOR_RIGHT\n")
                        f.write("	End of group\n")
                    
            else:
                for j in range(dig_map.shape[1]):
                    if dig_map[i, -j-1]:
                        f.write("		SELECT\n")
                        f.write("	End of group\n")
                        f.write("		SELECT\n")
                        f.write("	End of group\n")
                        
                    if j<dig_map.shape[1]-1:
                        f.write("		KEYBOARD_CURSOR_LEFT\n")
                        f.write("	End of group\n")
                    
            f.write("		KEYBOARD_CURSOR_DOWN\n")
            f.write("	End of group\n")
            
            i+=1
            
        f.write("		CUSTOM_CTRL_R\n")
        f.write("	End of group\n")
    
        f.write("End of macro\n")
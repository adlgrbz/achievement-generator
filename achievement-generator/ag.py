#!/usr/bin/python3

"""
Minecraft Achievement Generator
Author: Adil Gurbuz
Mail: adlgrbz@protonmail.com
"""

import generator
from os import listdir
from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog -t [text] -b [text] -i [item_name] output.png")
    parser.description = "Minecraft achievement generator"
        
    parser.add_option("-t", dest="TTEXT",
                      help="Top post for template")
    
    parser.add_option("-b", dest="BTEXT",
                      help="Subtitle for template")

    parser.add_option("-i", dest="ITEM",
                      help="Item name for template")
    
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("Missing or incorrect number of arguments")

    if not (options.ITEM) in listdir("./items"):
        name_list = ""
        for name in listdir("./items"):
            name_list += name.split(".")[0] + ", "
        parser.error("Icon name not found\n\nIcon name list:\n{}".format(name_list))

    generator.make([options.TTEXT, options.BTEXT], options.ITEM, args[0])

if __name__ == '__main__':
    main()

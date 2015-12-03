# Kristen Laguana
# CS294 Project
# Galaxy Sky Spaxel Logger

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--new", "-n", help="start on a new file",\
                    action="store_true")
parser.add_argument("--file", "-f", help="choose filename")
parser.add_argument("--working", "-w", help="work on existing file",\
                    action="store_true")
args = parser.parse_args()

# Welcome text

print('\nGalaxy Sky Spaxel Logger v1.0 by Kristen Laguana\n\n')

# if starting on a new file:
if args.new:
    print("Creating new file...")
#   print("File {} created. Let's begin.".format(args.file)
    out_file = open(args.file, 'w')

# if continuing from a previous working file:
if args.working:
    print("Retrieving working file...")
    out_file = open(args.file, 'a')

# if args == "--n":
# create new text file
# name file
# open file for writing and saving

#    fo = open("newfile.txt", "r+")
#    print "Filename: ", fo.name
#    new_fo = raw_input("Rename file (ex: foo.txt): ")
#    fo.name = new_fo
#    print "New filename: ", fo.name

# if args == "--w"
# prompt user for filename
# look up file
# open file for editing

# ********************************************

# assuming user wants to work on an existing file

# continue statement is temporary.
# if statement should probably be here
#existing_file = raw_input('Enter name of existing file (ex. filename.txt): ')
# file_object = open('existing_file', 'r+')
# ask user for filename
# search for filename and open it

# Spaxel by spaxel input? Y/N
# If Y then:
#   Go through entire 15x15 array

#   Print working spaxel (row, column)

#   "Type S to identify this spaxel as a sky spaxel.
#   Type N to mark this as a galaxy spaxel.
#   Type ? if you are unsure."

#   If S then:
#       Write spaxel to file
#   Else if ? then:
#       "Enable troubleshooting? Y/N"
# Else continue

# Is this a majority-sky cube? Y/N
# If Y then:
#   Input non-sky (or galaxy) spaxels (row, column), hit enter,
#   repeat for additional non-sky spaxels. When finished, type D.
#   Flag all of these spaxels
#   Go through entire 15x15 array
#   Input all spaxels into text file EXCEPT those that aren't flagged
# Else:
#   Input sky spaxels (row, column), hit enter, and repeat for
#   additional sky spaxels. When finished, type D.
#   Input all spaxels into text file

# Continue



# When encountering weird spaxel:
# Enable troubleshooting? Y/N

# Dictionary of common optical nebular spectral lines

lines = [['[OII] 3726', 3727.09],
         ['[OII] 3729', 3729.88],
         ['H12', 3751.22],
         ['H11',  3771.7],
         ['Ca II K', 3934.777],
         ['Ca II H', 3969.591],
         ['[OIII] 4363', 4364.44],
         [r'H$\beta$', 4862.70],
         ['[OIII] 5007', 5008.24],
         ['[OI] 5577', 5578.8874],
         ['He I', 5877.3],
         ['Na I 5890', 5891.583],
         ['Na I 5896', 5897.558],
         ['[OI] 6300', 6302.04],
         ['[NeII]', 6849.84],
         [r'H$\alpha$', 6564.61],
         ['[NII] 6583', 6585.23],
         ['HeI', 6679.996]]

def create_new_file():
    print("Creating new file...")
    pass

def begin_working_file():
    print("Retrieving file...")
    pass

# Kristen Laguana
# CS294 Project
# Galaxy Sky Spaxel Logger

import argparse

def create_new_file():
    print("Creating new file...\n")
    pass

def begin_working_file():
    print("Retrieving file...\n")
    pass

parser = argparse.ArgumentParser()
parser.add_argument("--new", "-n", help="start on a new file",\
                    action="store_true")
parser.add_argument("--file", "-f", help="choose filename")
parser.add_argument("--working", "-w", help="work on existing file",\
                    action="store_true")
args = parser.parse_args()

# Welcome text

print('\n// Galaxy Sky Spaxel Logger v1.0 by Kristen Laguana //\n\n')

# if starting on a new file:
if args.new:
    create_new_file()
    out_file = open(args.file, 'w')
    print("File {} created. Let's begin.\n".format(args.file))

# if continuing from a previous working file:
elif args.working:
    begin_working_file()
    out_file = open(args.file, 'a')
    print("Working file {} retrieved. Let's begin.\n".format(args.file))

# goes through 15x15 grid
for column in range(1, 16):
    for row in range(1,16):

        # prints working spaxel, prompts user for classification
        print("Currently at {},{}:\n".format(row,column))
        ans = raw_input("Is this a sky spaxel? (Y/N/?): ")
        
        # if user cannot classify spaxel
        if ans == "?":
            print("Diagnostics coming soon, sorry!\n")
        
        # if the spaxel is NOT a sky spaxel
        elif ans == "N":
            print("{},{} will be considered a galaxy spaxel.\n\
It will not be saved to the file.\n".format(row,column))
        
        # if the spaxel is a sky spaxel
        elif ans == "Y":
            
            # prompts user for confirmation
            out_file.write("{},{}".format(row,column))
            conf = raw_input("{},{} will be saved to file. \
Are you sure? (Y/N): ".format(row, column))

            # temp, replace w/whatever makes this return to line 45
            if conf == "N":
                print("WELP. TOO LATE 4 U\n")
            
            # saves spaxel to file
            elif conf == "Y":
               out_file.write("{},{}\n".format(row,column))
               print("{},{} will be saved to file as a sky spaxel.\n"\
               .format(row, column))
        else:
        # same problem as line 64
            print("Invalid input. Look at what you've gone and done.\n")
                

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

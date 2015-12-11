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

def classify():
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

                # temp, replace w/whatever makes this return to line 17
                if conf == "N":
                    classify()
                    # print("WELP. TOO LATE 4 U\n")
                
                # saves spaxel to file
                elif conf == "Y":
                   out_file.write("{},{}\n".format(row,column))
                   print("{},{} will be saved to file as a sky spaxel.\n"\
                   .format(row, column))
                else:
                    # same problem as line 17
                    classify() 

def main():
    global out_file

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

    classify()

    return

if __name__ == "__main__":
    main()

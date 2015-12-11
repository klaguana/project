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

def classify_spaxel(r,c):
    
    print("Currently at {},{}:\n".format(r, c))
    ans = raw_input("Is this a sky spaxel? (Y/N/?) : ")

    # if user cannot classify spaxel
    if ans.lower() == '?':
        print("Diagnostics coming soon, sorry!\n")

    # if the spaxel is NOT a sky spaxel
    elif ans.lower() == 'n':
        print("{},{} will be considered a galaxy spaxel.\n\
It will not be saved to file.\n".format(r,c))
    
    # if the spaxel is a sky spaxel
    elif ans.lower() == 'y':
        conf = raw_input("{},{} will be saved to file. \
Are you sure? (Y/N) : ".format(r,c))
        if conf.lower() == 'n':
            return classify_spaxel(r, c)

        else:
            out_file.write("{},{}\n".format(r, c))
            print("{},{} will be saved to file as a sky spaxel.\n"\
            .format(r, c))

def main():
    global out_file

    parser = argparse.ArgumentParser()
    parser.add_argument("--new", "-n", help = "start on a new file",\
                        action = "store_true")
    parser.add_argument("--file", "-f", help = "choose filename")
    parser.add_argument("--working", "-w", help = "work on existing file",\
                        action = "store_true")
    args = parser.parse_args()

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
        print("Working file {} retrieved. Let's begin.\n"\
        .format(args.file))

    # goes through 15x15 grid
    for c in range(1,16):
        for r in range(1,16):
            classify_spaxel(r, c)

    return

if __name__ == "__main__":
    main()

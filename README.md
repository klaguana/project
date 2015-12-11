# project
CS294 Project: Galaxy Sky Spaxel Logger

This program allows the user to properly classify spaxels from a 15x15 cube of spectra, and output sky spaxels into a text file for future sky subtraction. 

If working on a new cube:
$ python exp.py -n -f filename.txt

If working on an existing cube:
$ python exp.py -w -f filename.txt

Future goals:

1) Help the user diagnose spaxels that are unclear to user whether or not they contain sky spectra.

2) Output visual 15x15 grid that displays where the sky spaxels are in the cube (or lack thereof).

3) Output documentation of spaxel diagnostics (if diagnostics were needed).

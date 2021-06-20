#!/usr/bin/env python3
# Use sudo updatedb before searching for index all scripts in cache

import argparse
import re
import subprocess

from colorama import Fore, Style

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('-n', '--name', type=str)
parser.add_argument('-c', '--category', type=str)
parser.add_argument('-d', '--description', type=str)
parser.add_argument('-a', '--absolute-path', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-o', '--option', action='store_true')

HELP = '''Usage: searchnmapscript.py [--help] [--name NAME] [--category CATEGORY]
                           [--description DESCRIPTION] [--absolute-path] [--verbose | --option]

Options:
-h, --help                  Print this help summary page
-n, --name                  Script name for searching
-c, --category              Script category for searching
-d, --description           Script description for searching
-a, --absolute-path         Print scripts absolute paths (default: only names)
-v, --verbose               Verbose output (name / path + categories + description; default: name / path)
-o, --option                Output in option format for using in nmap scan'''

try:
    args = parser.parse_args()

    if args.help:
        print(HELP)
        exit(1)
    
    if args.verbose and args.option:
        print('Verbose option cannot be used with -o / --option option!')
        exit(1)

    scripts_absolute_path = subprocess.run(["locate", ".nse"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.strip().split('\n')
    description_regex = re.compile(r'description = \[\[.*?\]\]', flags=re.DOTALL | re.IGNORECASE)
    categories_regex = re.compile(r'categories = \{.*?\}', flags=re.DOTALL | re.IGNORECASE)
    index = 1
    output = ''

    for script_absolute_path in scripts_absolute_path:

        match = False
        script_name = script_absolute_path.split('/')[-1]
        script_description = str()
        script_categories = str()

        with open(script_absolute_path) as file:
            script_content = file.read()
            script_description = re.search(description_regex, script_content)
            if script_description:
                script_description = script_description.group(0)[17:-3]
            script_categories = re.search(categories_regex, script_content)
            if script_categories:
                script_categories = script_categories.group(0)[14:-1]

        if args.name:
            if re.search(args.name, script_name, flags=re.IGNORECASE):
                match = True

        if args.description:
            if script_description:
                if re.search(args.description, script_description, flags=re.IGNORECASE):
                    match = True

        if args.category:
            if script_categories:
                if re.search(args.category, script_categories, flags=re.IGNORECASE):
                    match = True

        if match == True:
            if not args.option:
                output += Style.RESET_ALL + '[' + str(index) + '] '
            endl = ', ' if args.option else '\n'
            if args.absolute_path:
                output += Style.BRIGHT + Fore.RED + script_absolute_path + endl
            else:
                output += Style.BRIGHT + Fore.RED + script_name + endl
            if args.verbose:
                if script_categories:
                    output += (Style.RESET_ALL + 'Categories: ' + Style.BRIGHT + Fore.BLUE + script_categories).strip('\n') + '\n'
                if script_description:
                    output += (Style.RESET_ALL + 'Description:\n' + Style.BRIGHT + Fore.BLUE + script_description).strip('\n') + '\n'
            index = index + 1

    print(output.strip(', ').strip('\n'))

except KeyboardInterrupt:
    raise SystemExit

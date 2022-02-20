__all__ = [
'bulk_rename',
'rename_file',
]

import re
import shutil
import sys
import logging
from pathlib import Path
import os
import argparse

'''
Program: bulk_renamer.py
Description: This program renames all the files in a directory(target_dir) that is
in the pattern(file_pattern) to a new name pattern(file pattern).
Developer: Mannix Tapawan (mannix.tapawan@gcash.com)
'''

#Configure logging
logging.basicConfig(level = logging.INFO)

def bulk_rename(new_name, file_pattern, target_dir):
    #Get all the files in the directory with the same pattern and rename to a new pattern
    direct = Path(target_dir).glob('*')
    file_pattern = re.compile(file_pattern)
    counter = 1
    for file in sorted(direct):
        file_name, file_ext = os.path.splitext(str(target_dir) + str(file))
        if file_pattern.match(file.name):
            new_filename = create_new_filename(new_name, counter, file_ext)
            rename_file(file, target_dir, new_filename)
            counter += 1
    return counter
    #logging.info("Total files renamed to pattern (" + new_name + '): ' + str(counter))

def create_new_filename(new_name, counter, extension):
    #Create the new file name 
    new_filename = f'{new_name}{counter}{extension}'
    return new_filename


def rename_file(file, target_dir, new_filename):
    #Rename file to the new filename
    shutil.move(file, (target_dir + '/' + new_filename))
    logging.info(str(file) + ' ---> ' + str(new_filename))

def main(args):
    try:
        bulk = bulk_rename(args.new_name, args.file_pattern, args.target_dir)
        if bulk:
            logging.info("Total files renamed to pattern (" + args.new_name + '): ' + str(bulk - 1))
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        logging.error("Exception: {}".format(e))
        sys.exit(1)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        'new_name',
        help = 'The new name of the file after renaming',
        )
        
    parser.add_argument(
        'file_pattern',
        help = 'The name pattern of the files you want to rename',
        )
        
    parser.add_argument(
        'target_dir',
        help = 'The folder of the files you want to rename',
        )
        
    args = parser.parse_args()

    main(args)
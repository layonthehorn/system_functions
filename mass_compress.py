#!/usr/bin/env python3

import glob, os, sys

keep = "keep"
remove = "remove"
message = f"Usage:\npypress ({remove}|{keep})" \
          f"\n{remove} - Deletes noncompressed copies\n{keep} - Keeps noncompressed copies"


# deletes old noncompressed files
def remove_com():
    com_methods = ("7zip", ".zip", ".7z", ".gz", ".rar", ".gzip", ".bzip2")
    for compress in glob.glob(os.path.join(os.getcwd(), "*")):
        file_name, file_ext = os.path.splitext(compress)
        if file_ext not in com_methods:
            file_base = os.path.basename(compress)
            compressed_name = file_base + ".tar.gz"
            os.system(f'tar -czvf "{compressed_name}" "{file_base}"')
            os.system(f'rm -rf "{file_base}"')


# keeps old noncompressed files
def keep_com():
    com_methods = ("7zip", ".zip", ".7z", ".gz", ".rar", ".gzip", ".bzip2")
    for compress in glob.glob(os.path.join(os.getcwd(), "*")):
        file_name, file_ext = os.path.splitext(compress)
        if file_ext not in com_methods:
            file_base = os.path.basename(compress)
            compressed_name = file_base + ".tar.gz"
            os.system(f'tar -czvf "{compressed_name}" "{file_base}"')


# checking arguments
if len(sys.argv) == 2:
    argument = sys.argv[1]
    if argument == keep:
        print("Keeping old files...")
    elif argument == remove:
        print("Removing old files...")
        agree = input("OK? (y/n) ").lower()
        if agree != "y":
            sys.exit(0)
    else:
        print(message)
        sys.exit(0)
else:
    print(message)
    sys.exit(0)

if argument == keep:
    keep_com()
elif argument == remove:
    remove_com()

#!/home/layonthehorn/.config/zsh_functions/env/bin/python3

import os
import subprocess

# this script will clear out my downloads folder
print("Clear downloads?")
answer = input("y/n ").lower()

# gets files in downloads folders
list_of_files = os.listdir("/mnt/Backups/Downloads/")
alt_downloads = os.listdir("/home/layonthehorn/Downloads/")
list_dir = ["/mnt/Backups/Downloads/", "/home/layonthehorn/Downloads/"]

# if there are none we cancel trying to delete anything
if (len(list_of_files) < 1 and len(alt_downloads) < 1) and answer == "y":
    print("Downloads folders are empty.")

# if there are some and we want to delete them we continue
elif answer == "y":
    for directory in list_dir:

        for file in os.listdir(directory):

            filesize = os.path.getsize(f"{directory}{file}")

            # if file is about .9 GB or greater in size asks if you mean to delete it
            if filesize >= 900000000:
                filesize = round(filesize / 900000000, 3)
                print(f"{file} is {filesize} GB. Do you want to delete it?")
                response = input("y/n ").lower()

                # checks for response from user
                if response == "y":
                    subprocess.run(["rm", "-rf", f"{directory}{file}"])
                    print(f"{file} removed...")
                else:
                    print(f"{file} not removed.")

            # if files is not too big just removes it
            else:
                subprocess.run(["rm", "-rf", f"{directory}{file}"])
                print(f"{file} removed...")

# cancels deleting anything
else:
    print("Operation canceled.")

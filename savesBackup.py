# Created by J. Rain
# 11/2022

# Needs 2-column .csv file with SOURCE_DIR,TARGET_DIR formatting.

import os
import shutil
import csv

def main():

    reader = csv.reader(open('steam_saves.csv', 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v
        
    for k, v in d.items():
    
        sourceDir = k
        print(sourceDir)
        targetDir = d[k]
        print(targetDir)

        saveFiles = os.listdir(sourceDir)
        
        for files in saveFiles:
            shutil.copy(os.path.join(sourceDir, files), targetDir)
            print(f"{sourceDir}{files} moved successfully.")
   
main()

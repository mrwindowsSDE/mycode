#!/usr/bin/env python3
#allows copying and moving around stuff
import shutil
#operating system dependent functionality
import os
os.chdir("/home/student/mycode/")
#copy file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copy the entire folder and subfolders to target directory
shutil.copytree("5g_research/", "5g_research_backup/")



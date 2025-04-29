#####"Rafi Lumen Log downloads for Developers"######
###################################################


import os
import shutil

#print(os.getcwd())  # Outputs the current working directory

src = "/mnt/efs/qa-lumen-logs/adminservice/lumen-2025-04-28.log"
dst = "/mnt/efs/tenant/liv-qa.assessappglobal.com.au/"

shutil.copy(src, dst)
print("*******Successfully Copied log*******")

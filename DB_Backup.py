##### Rafi DB Backup through Script #####
########################################

import os
import subprocess
import shutil
from datetime import date

today = date.today()
#.strftime("%d-%m-%Y")
os.environ["PGPASSWORD"] = "S4V05XN6aj2PKtthQ0"
tenant = "racds"
subprocess.run([
    "pg_dump",
    "-h", "assess-app-qa-rds-psql-readwrite.assessapp.com.au",
    "-U", "developer",
    f"{tenant}-qa.assessappglobal.com.au",
    "-f",f"{tenant}-qa.assessappglobal.com.au-"f"{today}.sql"
])
subprocess.run(["gzip",f"{tenant}-qa.assessappglobal.com.au-"f"{today}.sql"])

print(f"{tenant}-qa.assessappglobal.com.au-"f"{today}.sql",subprocess.run(["du","-h",f"{tenant}-qa.assessappglobal.com.au-"f"{today}.sql.gz"]))


shutil.move(
    f"{tenant}-qa.assessappglobal.com.au-"f"{today}.sql.gz",
    "/mnt/efs/qa-backups/deployment-backups"
)

print("DB Downloaded!!!!")

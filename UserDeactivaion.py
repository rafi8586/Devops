#*****************Rafi User Deactivation***************************#

import os
import subprocess

#print(os.getcwd())
os.environ["PGPASSWORD"] = "S4V05XN6aj2PKtthQ0"

tenants = [
    "racds-qa.assessappglobal.com.au",
    "monashabdr-qa.assessappglobal.com.au",
    "sandbox-qa.assessappglobal.com.au",
    "racds-qa.assessappglobal.com.au",
    "ambersoft-qa.assessappglobal.com.au",
    "liv-qa.assessappglobal.com.au",
    "racs-qa.assessappglobal.com.au",
    "racpdss-qa.assessappglobal.com.au",
    "ranzcowba-qa.assessappglobal.com.au",
    "saas-qa.assessappglobal.com.au",
    "acddermpoint-qa.assessappglobal.com.au",
    "standalone-qa.assessappglobal.com.au",
    "monashabdr-qa.assessappglobal.com.au",
    "sandbox-qa.assessappglobal.com.au",
    "specialist-qa.assessappglobal.com.au",
    "demo.assessappglobal.com.au",
    "demo-ai.assessappglobal.com.au"
]

for tenant in tenants:
    print(f"\nRunning query for tenant DB: {tenant}")
    subprocess.run([
        "psql",
        "-h", "assess-app-qa-rds-psql-readwrite.assessapp.com.au",
        "-U", "developer",
        "-d", tenant,
        "-c", "SELECT * FROM users WHERE email LIKE 'rafi@eluminaelearning.com.au';",
       # "-c", "UPDATE users SET status = 0 WHERE email IN ('rafi@eluminaelearning.com.au');",
    ])

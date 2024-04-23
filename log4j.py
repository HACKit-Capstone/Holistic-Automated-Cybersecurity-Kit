from os import system
import sys

msg = sys.argv[1]
burp = input("Enter Burp collabrator client id address or interactsh domain address (yrt45r4sjyoj19617jem5briio3cs.burpcollaborator.net): ")

system(f"bash Log4j-RCE-Scanner/log4j-rce-scanner.sh -l {msg}.txt -b {burp} | tee -a {msg}log4j.txt")

print(f"Log4j vulnerabilities saved to: {msg}log4j.txt")

# system(f"cat tee -a {msg}log4j.txt | notify")
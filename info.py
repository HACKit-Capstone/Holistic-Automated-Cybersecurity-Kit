from os import system
import sys

msg = sys.argv[1]

system(f"cat {msg}.txt | waybackurls | httpx -mc 200 -ct | grep application/json | tee -a {msg}info.txt")

print(f"Information Disclosure saved to: {msg}info.txt")
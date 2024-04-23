from os import system
import sys

msg = sys.argv[1]

system(f"cat {msg}.txt | httpx | while read url; do target=$(curl -s -I -H 'Origin: https://evil.com' -X GET $url); if echo $target | grep -q 'https://evil.com'; then echo '[Potential CORS Found]' $url; fi; done | tee -a {msg}cors.txt")
system(f"cat {msg}urls.txt | httpx | while read url; do target=$(curl -s -I -H 'Origin: https://evil.com' -X GET $url); if echo $target | grep -q 'https://evil.com'; then echo '[Potential CORS Found]' $url; fi; done | tee -a {msg}cors.txt")
system(f"assetfinder {msg} | httpx -threads 300 -follow-redirects -silent | rush -j200 'curl -m5 -s -I -H \"Origin: evil.com\" {msg} | grep -q \"evil.com\" && printf \"\n\033[0;32m[VUL TO CORS] - {msg}\e[m\" || true' | tee -a {msg}cors.txt")
#system(f"curl -I -H 'Origin: https://evil.com' 'https://{msg}/api.php'")

system("sort {}cors.txt | uniq > {}cors_sorted.txt".format(msg, msg))
system("rm -rf {}cors.txt".format(msg))
system("mv {}cors_sorted.txt {}cors.txt".format(msg, msg))
system("rm -rf {}cors_sorted.txt".format(msg))

print(f"CORS vulnerabilities saved to: {msg}cors.txt")

# system(f"cat tee -a {msg}cors.txt | notify")
from os import system

msg = input("Enter the target (bing.com): ")

system(f"cat {msg}.txt | httpx | while read url; do target=$(curl -s -I -H 'Origin: https://evil.com' -X GET $url); if echo $target | grep -q 'https://evil.com'; then echo '[Potential CORS Found]' $url; fi; done")
system(f"assetfinder {msg} | httpx -threads 300 -follow-redirects -silent | rush -j200 'curl -m5 -s -I -H \"Origin: evil.com\" {msg} | grep -q \"evil.com\" && printf \"\n\033[0;32m[VUL TO CORS] - {msg}\e[m\" || true'")
system(f"curl -I -H 'Origin: https://evil.com' 'https://{msg}/api.php'")

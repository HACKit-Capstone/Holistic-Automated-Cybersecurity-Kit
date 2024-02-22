from os import system
import sys

msg = sys.argv[1]

# system('cat {}.txt | waybackurls > {}urls.txt')

# system("cat {}.txt | while read url; do python3 tplmap.py -u $url; echo $url; done".format(msg))

ssti_urls = []

system('cat {}urls.txt | qsreplace "abc{{9*9}}" > {}fuzz.txt'.format(msg, msg))
system("ffuf -u FUZZ -w {}fuzz.txt -replay-proxy http://127.0.0.1:8080 > {}ssti.txt".format(msg, msg))
system("rm -rf {}fuzz.txt".format(msg))

with open('{}ssti.txt'.format(msg), 'r') as output_file:
    lines = output_file.readlines()
    for line in lines:
        if "abc81" in line:
            ssti_urls.append(line.strip())

print("URLs with identified SSTI:")
for ssti_url in ssti_urls:
    print(ssti_url)

vulnerable_urls_file = '{}vulnerable_urls.txt'.format(msg)
with open(vulnerable_urls_file, 'w') as output:
    output.write("Vulnerable URLs:\n")
    for url in ssti_urls:
        output.write(url + '\n')

# print(f"Vulnerable URLs saved in '{vulnerable_urls_file}' file.")

system("rm -rf {}ssti.txt".format(msg))
system("sort {}vulnerable_urls.txt | uniq > {}ssti.txt".format(msg, msg))
system("rm -rf {}vulnerable_urls.txt".format(msg))

print(f"SSTI vulnerabilities saved to: {msg}ssti.txt")

# system(f"cat tee -a {msg}ssti.txt | notify")


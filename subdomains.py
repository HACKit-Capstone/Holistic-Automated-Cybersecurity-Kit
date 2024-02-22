from os import system
import sys

msg = sys.argv[1]

system("curl -s 'https://crt.sh/?q={}' | grep '<TD>' | grep {} | cut -d '>' -f2 | cut -d '<' -f1 | sort -u | sed '/^*/d' | tee -a {}.txt".format(msg,msg,msg))
system("curl -s 'https://rapiddns.io/subdomain/{}#result' | grep '<td><a' | cut -d '\"' -f 2 | grep http | cut -d '/' -f3 | sed '/^*/d' | tee -a {}.txt".format(msg,msg))
system("curl -s 'https://jldc.me/anubis/subdomains/{}' | grep -Po '((http|https):\/\/)?(([\w.-])\.([\w])\.([A-z]))\w+' | cut -d '/' -f3 | sort -u | tee -a {}.txt".format(msg,msg))
system("subfinder -d {} | tee -a {}.txt".format(msg,msg))
# system("subfinder -d {} -silent | dnsx -silent | cut -d ' ' -f1  | grep --color 'api\|dev\|stg\|test\|admin\|demo\|stage\|pre\|vpn' | tee -a {}.txt".format(msg,msg))
system("curl -s https://dns.bufferover.run/dns?q=.{} | jq -r .FDNS_A[] | cut -d',' -f2 | sort -u | tee -a {}.txt".format(msg,msg))
system("curl -s 'http://web.archive.org/cdx/search/cdx?url=*.{}/*&output=text&fl=original&collapse=urlkey' | sed -e 's_https*://__' -e 's/\/.*//' | sort -u | tee -a {}.txt".format(msg, msg))
system('curl -s "https://jldc.me/anubis/subdomains/{}" | grep -Po "((http|https)://)?(([\w.-]*).([\w]*).([A-z]))w+" | sort -u | tee -a {}.txt'.format(msg, msg))
system('curl -s "https://crt.sh/?q=%25.{}&output=json" | jq -r ".[].name_value" | sed "s/\\*\\.//g" | sort -u | tee -a {}.txt'.format(msg, msg))
system('curl -s "https://jldc.me/anubis/subdomains/{}" | jq -r "." | grep -o "\\w.*{}" | tee -a {}.txt'.format(msg, msg, msg))
system('curl -s "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}" | jq -r ".subdomains" | grep -o "\\w.*{}" | tee -a {}.txt'.format(msg, msg, msg))
system('curl -s "https://otx.alienvault.com/api/v1/indicators/domain/{}/url_list?limit=100&page=1" | grep -o \'"hostname": *"[^"]*\' | sed \'s/"hostname": "//\' | sort -u | tee -a {}.txt'.format(msg, msg))
system('curl -s "https://riddler.io/search/exportcsv?q=pld:{}" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u | tee -a {}.txt'.format(msg, msg))
system('curl -s "https://api.certspotter.com/v1/issuances?domain={}&include_subdomains=true&expand=dns_names" | jq .[].dns_names | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u | tee -a {}.txt'.format(msg, msg))
system('curl -s "https://api.hackertarget.com/hostsearch/?q={}" | awk -F, \'{{print $1 "\\n" $2}}\' | tee -a {}.txt'.format(msg, msg))
system('curl -s "https://api.hackertarget.com/hostsearch/?q={}" | awk -F, \'{{print $1 "\\n" $2}}\' | tee -a {}.txt'.format(msg, msg))
system("python3 ctfr/ctfr.py -d {} -o {}.txt".format(msg,msg))
system("nmap --script hostmap-crtsh.nse {} | grep -oE '[a-zA-Z0-9_-]+\.{}' | sort -u | tee -a {}.txt".format(msg, msg, msg))

system("sort {}.txt | uniq > {}_sorted.txt".format(msg, msg))
system("rm -rf {}.txt".format(msg))
system("mv {}_sorted.txt {}.txt".format(msg, msg))
system("rm -rf {}_sorted.txt".format(msg))

print(f"Subdomains saved to: {msg}.txt")

system("waybackurls {} > {}urls.txt".format(msg, msg))

# system("curl --request GET --url 'https://reconapi.redhuntlabs.com/community/v1/domains/subdomains?domain=<{}>&page_size=1000' --header 'X-BLOBR-KEY: API_KEY' | jq '.subdomains[]' -r | tee -a {}.txt".format(msg,msg))

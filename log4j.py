import os

msg = input("Enter the target (bing.com): ")

os.chdir("log4j-scan")

os.system("cat ../" + msg + ".txt | httpx | xargs -I@ sh -c 'python3 log4j-scan.py -u @ --run-all-tests --dns-callback-provider dnslog.cn'")

os.chdir("..")

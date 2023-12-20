from os import system
import sys

msg = sys.argv[1]

system("sort {}.txt | uniq | sed '/^*/d' | tee -a {}".format(msg,msg))
system(f"cat {msg} | httpx -o {msg}")
system("nuclei -update-templates")
system(f"nuclei -l {msg} -t nuclei-templates/ -severity critical,high,medium,low | tee -a {msg}nuclei.txt")

# system(f"cat tee -a {msg}nuclei.txt | notify")
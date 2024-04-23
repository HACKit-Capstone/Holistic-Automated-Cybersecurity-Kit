import subprocess
from pyfiglet import Figlet
from termcolor import colored
from tqdm import tqdm
import time
import sys

def print_banner():
    custom_fig = Figlet(font='banner3-D')  
    ascii_text = custom_fig.renderText('HACKit')
    colored_ascii_text = colored(ascii_text, 'blue')

    print(colored_ascii_text, end='')
    print(" ")
    print('Welcome to HACKit: Holistic Automated CyberSecurity Kit!')
    print('_____________________________________________________________________________________________________________')
    print(' ')
    print('HACKit is a tool that automates the process of penetration testing. It is a tool which has access to exploit multiple bugs simultaneously.')
    print('_____________________________________________________________________________________________________________')
    print(' ')

def main():
    print_banner()

    msg = input("Input the target you want to exploit (bing.com): ")
    print('_____________________________________________________________________________________________________________')
    print(' ')
    print('Below you can choose from options to exploit the bug from the choices.')
    print(' ')
    print('1. CORS (Cross-origin resource sharing)')
    print('2. Prototype-pollution')
    print('3. LFI (Local File Inclusion)')
    print('4. Open-redirect')
    print('5. SSTI (Server-side Template Injection)')
    print('6. Log4j vulnerabiltity')
    print('7. XSS (Cross Site Scripting)')
    print('8. SQLi (SQL Injection)')
    print('9. CRLF Injection (Carriage Return and Line Feed Injection)')
    print('10. Nuclei')
    print('11. Subdomain Takeover')
    print('12. Information Disclosure')
    print('13. Exploit all at once')
    print('14. Exit')
    print('_____________________________________________________________________________________________________________')
    print(' ')

    choices = input("Choose your options (comma-separated): ").split(',')
    choices = [int(choice.strip()) for choice in choices]

    if 14 in choices:
        print('You chose to exit. Thank you for using HACKit. Comeback soon!')
        for i in tqdm(range(100), ascii=False, ncols=75):
            time.sleep(0.03)
        print('_____________________________________________________________________________________________________________')
        print(' ')
        sys.exit(0)
        
    print(f'You chose options {choices}. HACKit is working on the selected vulnerabilities...')
    for i in tqdm(range(100), ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')

    vulnerability_scripts = {
        1: 'cors.py',
        2: 'prototype-pollution.py',
        3: 'lfi.py',
        4: 'open-redirect.py',
        5: 'ssti.py',
        6: 'log4j.py',
        7: 'xss.py',
        8: 'sqli.py',
        9: 'crlf.py',
        10: 'nuclei.py',
        11: 'subdom-tk.py',
        12: 'info.py'
    }
    
    if any(0 < choice < 14 for choice in choices):
        subprocess.run(['python3', 'subdomains.py', msg])

    selected_scripts = [vulnerability_scripts.get(choice) for choice in choices if choice != 13]
    if 13 in choices:
        selected_scripts.extend(vulnerability_scripts.values())

    for script in selected_scripts:
        if script:
            subprocess.run(['python3', script, msg])
        else:
            print(f'Invalid choice in {choices}. Please make a valid selection.')

if __name__ == "__main__":
    main()

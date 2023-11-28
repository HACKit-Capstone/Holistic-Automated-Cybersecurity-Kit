from pyfiglet import Figlet
from termcolor import colored
from tqdm import tqdm
import time

custom_fig = Figlet(font='banner3-D')  
ascii_text = custom_fig.renderText('HACKit')
colored_ascii_text = colored(ascii_text, 'blue')

print(colored_ascii_text, end='')

print(" ")

print('Welcome to HACKit: Holistic Automated CyberSecurity Kit!')

print('_____________________________________________________________________________________________________________')
print(' ')

print('HACKit is a tool that automates the process of penetration testing. It is a tool which has access to exploit multiple bugs simultaneously or together.')

print('_____________________________________________________________________________________________________________')
print(' ')

domain = input("Input the domain you want to exploit: ")

print('_____________________________________________________________________________________________________________')
print(' ')

print('Below you can choose from options to exploit the bug from the choices.')

print(' ')

print('1. SSTI (Server-side Template Injection)')
print('2. SQLi (SQL Injection)')
print('3. Open-redirect')
print('4. CORS (Cross-origin resource sharing)')
print('5. CRLF Injection (Carriage Return and Line Feed Injection)')
print('6. LFI (Local File Inclusion)')
print('7. Log4j vulnerabiltity')
print('8. XSS (Cross Site Scripting)')
print('9. Prototype-pollution')
print('10. Exploit all at once')
print('11. Exit')

print('_____________________________________________________________________________________________________________')
print(' ')

choice = int(input("Choose your option: "))

if choice == 1:
    print('You choose 1. HACKit working on SSTI...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the SSTI File

elif choice == 2:
    print('You choose 2. HACKit working on SQLi...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the SQLi File

elif choice == 3:
    print('You choose 3. HACKit working on Open-redirect...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the Open-redirect File

elif choice == 4:
    print('You choose 4. HACKit working on CORS...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the CORS File

elif choice == 5:
    print('You choose 5. HACKit working on CRLF...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the CRLF File

elif choice == 6:
    print('You choose 6. HACKit working on LFI...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the LFI File

elif choice == 7:
    print('You choose 7. HACKit working on Log4j...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the Log4j File

elif choice == 8:
    print('You choose 8. HACKit working on XSS...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the XSS File

elif choice == 9:
    print('You choose 9. HACKit working on Prototype-pollution...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call the Prototype-pollution File

elif choice == 10:
    print('You choose 10. HACKit working on exploiting all available vulnerabilities at once...')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Call all files

elif choice == 11:
    print('You choose 11. Thank you for using HACKit. Comeback soon!')
    for i in tqdm (range (100),
               ascii=False, ncols=75):
        time.sleep(0.03)
    print('_____________________________________________________________________________________________________________')
    print(' ')
    #Exit from all

else:
    print('Invalid choice. Please make a choice again.')
    #Redirect again to choosing the correct input.
    



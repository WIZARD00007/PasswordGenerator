import colorama
from colorama import Fore
from termcolor import colored
from pyfiglet import Figlet
from itertools import permutations
from string import ascii_lowercase
f=Figlet(font='standard')
print(colored(f.renderText('Password'),'blue'))
print(colored(f.renderText('Generator'),'red'))
textname=input(Fore.RED+'Enter a file name :')
try:
    pas=input(Fore.GREEN+'Enter a path to store passwords :')
    pas1=pas+'/'+ textname +'.txt'
    fileop=open(pas1,'w+')
    file2=open(pas1,'a+')
    leng=int(input(Fore.BLUE+'Enter the length of password :'))
    alp=input(Fore.BLUE+"Enter characters here (ex:abcd123#@) :")
    a=[]
    a[:0]=alp
    xpass=permutations(alp,leng)
    count=0
    for i in list(xpass):
       count=count+1
       str=''.join(i)
       if str not in file2:
          file2.write(str)
          file2.write('\n')
    print(f"{Fore.GREEN} password file {textname}.txt containing {count} passwords saved at {pas}")
    file2.close()
except:
  print(f"{Fore.RED} pleaae check your path")
  exit()

import os
import time
from tqdm import *
from pyfiglet import Figlet
import requests
import random
import itertools
import sys
import pyqrcode
import barcode
from queue import Queue
import socket
import threading
from barcode import EAN13
from barcode.writer import ImageWriter

from pip._vendor.distlib.compat import raw_input
import pyfiglet
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

result = pyfiglet.figlet_format("RECON TOOL",font="5lineoblique")
print(result)
options =(
    "\n 1- MY IP ADDRESS \n 2- PASSWORD GENERATOR\n 3- WORDLIST GENERATOR\n 4-BARCODE GENERATOR\n 5- QRCODE GENERATOR\n 6- PHONE NUMBER INFO\n 7- SUBDOMAIN SCANNER\n 8- PORT SCANNER\n 9- DDOS ATTACK\n"
)
print(options)
select=int(input("ENTER YOUR CHOICE "R""">>>>----------------->"""))

match select:
    case 1:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Loading Done!!")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        

        def window_size(columns=750,height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("FIND MY IP"))
            loading()

            hostname = socket.gethostname()
            IPaddr = socket.gethostbyname(hostname)
            print("YOUR DEVICE IS: "+ hostname)
            print("YOUR IP ADDRESS IS: "+IPaddr)
            raw_input("PRESS ENTER TO EXIT")
    

    case 2:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=75):
            os.system("clear")
            os.system('cols %s rows %s'%(columns,height))

        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("PASSWORD GENERATOR"))
            loading()
            length = int(input("ENTER THE LENGTH OF THE PASSWORD "r""">>>>----------->"""))

        def get_random_string(length):
            lower= "abcdefghijklmnopqrstuvwxyz"
            upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers= "0123456789"
            symbols= "!@#$%^&*()[]{}/?"
            all= lower+upper+numbers+symbols
            password = "".join(random.sample(all,length))
            print("GENERATED PASSWORD OF LENGTH",length," is ",password,r""">>>>>--------->""")

        get_random_string(length)
        raw_input(" PRESS ENTER TO EXIT")

    case 3:

        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=75):
            os.system("clear")
            os.system('cols %s rows %s'%(columns,height))
        
        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("WORDLIST GENERATOR"))
            loading()
            print("GENERATED PASSWORD IS SAVED IN THE PRESENT DIRECTORY")
            chrs = raw_input("ENTER THE LETTERS FOR COMBINATION"r""">>>>--------->""")
            l = int(input("MINIMUM LENGTH OF THE PASSWORD "r""">>>>--------->"""))
            k=l
            j=int(raw_input("MAXIMUM LENGTH OF THE PASSWORD "r""">>>>--------->"""))
            n=j+1
            mtl= len(chrs)
            p=[]
            zt = raw_input("[+] Enter the name of the file"r""">>>>--------->""")
            for ltp in range(k,n):
                ans = mtl**ltp
                p.append(ans)
                tLine = sum(p)
                raw_input("ARE YOU READY???[PRESS ENTER]")
                time1 = time.asctime()
                start = time.time()
                psd =open(zt,'a')

                for i in range(k,n):
                    r = (i-k+1)* 100/(n-k)
                    l = str(r) + ' percent '
                    sys.stdout.write("\r%s" % l)
                    sys.stdout.flush()
                    psd.flush()

                    for xs in itertools.product(chrs, repeat=i):
                        psd.write(''.join(xs)+'\n')
                        psd.flush()

            psd.close()
            sys.stdout.write(" SUCCESS ")
            end= time.time()
            totaltime = end - start
            rate= tLine/totaltime
            raw_input("PRESS ENTER TO EXIT")

    case 4:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=75):
            os.system("clear")
            os.system('cols %s rows %s'%(columns,height))

        def generator(number):
            my_code = EAN13(number, writer = ImageWriter())
            my_code.save("barcode") 
        
        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("BARCODE GENERATOR"))
            loading()
            print("GENERATED BARCODE WILL BE SAVED AS PNG IN THE PRESENT DIRECTORY")
            innumber = input("Enter 12 digit number to generate bar code"r">>>>----------->""")
            print(innumber)
            generator(innumber)
            raw_input("PRESS ENTER TO EXIT")

    case 5:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=75):
            os.system("clear")
            os.system('cols %s rows %s'%(columns,height))

        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("QRCODE GENERATOR"))
            loading()
            print("GENERATED QRCODE WILL BE SAVED AS MYQR.PNG IN THE PRESENT DIRECTORY")

            s = input("ENTER THE LINK TO CREATE A NEW QRCODE"r""">>>>---------->""")
            url = pyqrcode.create(s)
            url.svg("myqr.svg",scale=8)
            url.png("myqr1.png",scale=6)
            raw_input("PRESS ENTER TO EXIT")

    case 6:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=75):
            os.system("clear")
            os.system('cols %s rows %s'%(columns,height))

        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("PHONE NUMBER INFO"))
            loading()
            
            def num_scanner(phn_num):
                number = phonenumbers.parse(phn_num)
                print(number)
                description = geocoder.description_for_number(number,'en')
                supplier = carrier.name_for_number(number,'en')
                info = [["country", "SUPPLIER"],[description,supplier]]
                data = str(tabulate(info,headers="firstrow",tablefmt="github"))
                return data
            number = input("ENTER THE NUMBER"r""">>>>-------------->""")
            print(num_scanner(number))
            raw_input("PRESS ENTER TO EXIT")

    case 7:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=75):
            os.system("clear")
            os.system('cols %s rows %s'%(columns,height))
        
        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("SUBDOMAIN SCANNER"))
            loading()
            print("IT TAKES TIME ACCORDING TO THE DOMAIN")
            print("USINT DEFAULT ADDED WORDLIST WITH 649649 WORDS")
            domain = input("ENTER THE DOMAIN TO SCAN"r""">>>>------>""")
            file= open("subdomain.txt")
            content = file.read()
            subdomains = content.splitlines()
            for subdomain in subdomains:
                url = "http://"+subdomain+"."+domain
                try:
                    requests.get(url)
                    print("[+]Discovered subdomain: ",url)
                except requests.ConnectionError:
                    print("[+] Subdomain not found:",url)
            raw_input("PRESS ENTER TO EXIT")
        
    case 8:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=75):
            os.system("clear")
            os.system('cols %s rows %s'%(columns,height))

        def portscan(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target,port))
            except:
                return False
            
        def get_ports(mode):
            if mode==1:
                for port in range(1,1024):
                    queue.put(port)
            elif mode==2:
                for port in range(1,49152):
                    queue.put(port)
            elif mode==3:
                ports=[20,21,22,23,25,53,80,110,443]
                for port in ports:
                    queue.put(port)
            elif mode==4:
                ports = input("Enter your ports (seperate by blank):")
                ports= ports.split()
                ports = list(map(int,ports))
                for port in ports:
                    queue.put(port)

        def worker():
            while not queue.empty():
                port = queue.get()
                if portscan(port):
                    print("[+] Port {} is open".format(port))
                    open_ports.append(port)
        def run_scanner(threads, mode):
            get_ports(mode)
            thread_list=[]

            for t in range(threads):
                thread= threading.Thread(target=worker)
                thread_list.append(thread)

            for thread in thread_list:
                thread.start()
            for thread in thread_list:
                thread.join()
            print("open ports are: ",open_ports)
    
        if __name__== "__main__":
            window_size(columns=80,height=20)
            print(font("PORT SCANNER"))
            loading()
            print("IT TAKES TIME ACCORDING TO THE PROVIDED IP")
            target = input("ENTER THE IP TO SCAN"r""">>>>------------------>""")
            mode =int(input("Enter port scan mode(1-4): "))
            queue=Queue()
            open_ports=[]
            run_scanner(100,mode)

    case 9:
        def loading():
            for _ in tqdm(range(100),desc="Loading...",ascii=False,ncols=60):
                time.sleep(0.01)
            print("Let's move!!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        
        def window_size(columns=750,height=30):
            os.system("cls")
            os.system('cols %s rows %s'%(columns,height))
        if __name__ == "__main__":
            window_size(columns=80,height=20)
            print(font("DDOS"))
            loading()
            
            target=raw_input("ENTER THE IP ADDRESS"r""">>>>>-----------""")
            port = int(input("ENTER THE PORT "r""">>>>-------------->"""))
            fake_ip = '198.168.1.115'
            already_connected= 0

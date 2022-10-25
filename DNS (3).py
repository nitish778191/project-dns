
import socket
from tkinter import *
import time

#root.mainloop()
class TrieNode:
    def __init__(self):
        self.child = [None] * 27
        self.ip = None
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def getIndex(self, c):
        # For the . (dot) in IP address, we'll use the 10th index in child list
        return 26 if c == '.' else (ord(c) - ord('a'))

    def insert(self, domain, ipa):
        cur = self.root
        n = len(domain)

        for level in range(n):
            # We'll use the digits of IP address to form the trie structure
            idx = self.getIndex(domain[level])

            if cur.child[idx] is None:
                # Create a new trie node if not available for a particular digit
                # and assign to the respective index
                cur.child[idx] = TrieNode()

            cur = cur.child[idx]

        # At the end, we'll map the domain name and mark the end node
        cur.ip = ipa
        cur.is_end = True

    def search_ip(self, domain1):
        cur = self.root
        n = len(domain1)
        global domain, flag

        # Traverse through the trie structure with all digits in ip address
        for level in range(n):
             idx = self.getIndex(domain1[level])
            if cur.child[idx] is None:
                flag += 1
                domain.append(domain1)
                str2 = socket.gethostbyname(domain1)
                ip.append(str2)
                return f'Domain Name not found in DNS-Cache \n\nThe {domain1} IP Address is {socket.gethostbyname(domain1)}'


            cur = cur.child[idx]

        # Returns the url when all the digits in ip found
        if cur and cur.ip:
            flag = 2
            return f'Found in DNS-Cache\n\nThe {domain} IP Address is {cur.ip}'

        return f'Domain Name not found in DNS-Cache\n\nThe {domain} IP Address is {socket.gethostbyname(domain)}'


# Driver Code
flag=0

ip = ["107.108.11.123", "107.109.123.255", "74.125.200.106"]
domain = ["www.samsung.com", "www.samsung.net", "www.youtube.com"]

trie = Trie()
while(flag!=2):
    for idx in range(len(domain)):
        trie.insert(domain[idx], ip[idx])

    print("Enter domain name:")
    dom = ""
    root = Tk()

    root.geometry("400x450")
    root.minsize(900,450)
    root.title("DNS Cache")

    Label(text="Enter Domain Name",font="lucid 36 bold",pady=3,bg="grey",borderwidth=1,relief=SUNKEN).pack(pady=6,fill=X)
    domainget = StringVar()
    domainentry = Entry(root,textvariable=domainget)
    domainentry.pack(pady=6)

    def getval():
        global dom
        dom  = domainget.get()
        print(dom)
        furthercall()
    buttontext = StringVar()
    b1 = Button(textvariable=buttontext,command=getval,font="Raleway",bg="grey",pady=8)
    buttontext.set("Search")
    b1.pack(pady=8)

    text_box = Text(root,height=10,width=85,padx=85,pady=15,font="Courier 16 italic")
    text_box.pack(fill=X)


     #dom=input()

    def furthercall():
        start = time.process_time()
        str1 = trie.search_ip(dom)

        end=time.process_time()
        t = (end-start)*1000
        final =  "Time Elapsed:" + str(t) + "\n" + str1
        text_box.insert(1.0,final)
    #print(trie.search_ip("www.leetcode.com"))

    root.mainloop()
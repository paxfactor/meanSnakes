#!/usr/bin/python

# A simple script to compare hashed passwords
import crypt
import sys

def testPass(cryptPass, dictList):
    salt = cryptPass[0:2]
    dictFile = open(dictList, 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+word+"\n"
            return
    print "[-] Password Not Found.\n"
    return

def checkFile(passFile, dictList):
    passList = open(passFile, 'r')
    for line in passList.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For "+user
            testPass(cryptPass, dictList)

def main():
    passFile = raw_input("Enter password file: ")
    dictList = raw_input("Enter dictionary: ")
    checkFile(passFile, dictList)

if __name__ == "__main__":
    main()

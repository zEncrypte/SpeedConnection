import os
import sys
import ctypes
import speedtest
from pystyle import Colors, Colorate, Center
from time import sleep
from datetime import datetime

uwu = "Connection Speed"
ctypes.windll.kernel32.SetConsoleTitleW(uwu)

os.system("cls")
print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red, '''

╭━━━╮ ╭━━━╮ ╭━╮ ╭╮ ╭━╮ ╭╮ ╭━━━╮ ╭━━━╮ ╭━━━━╮╭━━╮ ╭━━━╮ ╭━╮ ╭╮ 
┃╭━╮┃ ┃╭━╮┃ ┃┃╰╮┃┃ ┃┃╰╮┃┃ ┃╭━━╯ ┃╭━╮┃ ┃╭╮╭╮┃╰┫┣╯ ┃╭━╮┃ ┃┃╰╮┃┃ 
┃┃ ╰╯ ┃┃ ┃┃ ┃╭╮╰╯┃ ┃╭╮╰╯┃ ┃╰━━╮ ┃┃ ╰╯ ╰╯┃┃╰╯ ┃┃  ┃┃ ┃┃ ┃╭╮╰╯┃ 
┃┃ ╭╮ ┃┃ ┃┃ ┃┃╰╮┃┃ ┃┃╰╮┃┃ ┃╭━━╯ ┃┃ ╭╮   ┃┃   ┃┃  ┃┃ ┃┃ ┃┃╰╮┃┃ 
┃╰━╯┃ ┃╰━╯┃ ┃┃ ┃┃┃ ┃┃ ┃┃┃ ┃╰━━╮ ┃╰━╯┃   ┃┃  ╭┫┣╮ ┃╰━╯┃ ┃┃ ┃┃┃ 
╰━━━╯ ╰━━━╯ ╰╯ ╰━╯ ╰╯ ╰━╯ ╰━━━╯ ╰━━━╯   ╰╯  ╰━━╯ ╰━━━╯ ╰╯ ╰━╯
╭━━━╮ ╭━━━╮ ╭━━━╮ ╭━━━╮ ╭━━━╮
┃╭━╮┃ ┃╭━╮┃ ┃╭━━╯ ┃╭━━╯ ╰╮╭╮┃
┃╰━━╮ ┃╰━╯┃ ┃╰━━╮ ┃╰━━╮  ┃┃┃┃
╰━━╮┃ ┃╭━━╯ ┃╭━━╯ ┃╭━━╯  ┃┃┃┃
┃╰━╯┃ ┃┃    ┃╰━━╮ ┃╰━━╮ ╭╯╰╯┃
╰━━━╯ ╰╯    ╰━━━╯ ╰━━━╯ ╰━━━╯

''', 1)))
print()
txt = " [-] This program will measure u Internet Speed"
print(Center.XCenter(Colorate.Color(Colors.cyan, txt, True)))
print()

servers = []
threads = None
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()
results_dict = s.results.dict()

DL = round(results_dict['download']/(1024*1024), 2)
UP = round(results_dict['upload']/(1024*1024), 2)
ping = round(results_dict['ping'], 0)

if __name__ == "__main__":
    print('Download: ', DL, Colorate.Color(Colors.pink, 'Mbps'))
    print('Upload: ', UP, Colorate.Color(Colors.turquoise, 'Mbps'))
    print('Ping: ', ping, Colorate.Color(Colors.light_green, 'ms'))

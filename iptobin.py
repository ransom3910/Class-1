#!/usr/bin/env python
import sys

ot = []
c = 0
zeros = ""
if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
    if ip_addr[0:1]=="-":
        if ip_addr=="-h" or ip_addr=="-?":
            print("Enter an ip address after iptobin.  Example iptobin 192.168.1.1")
            exit(0)
        elif ip_addr=="-a":
            print("IP to binnary converter by Mike Ransom")
            exit(0)
        else:
            print("Valid options are ? -h -? -a /h /? /a")
            exit(0)

    if ip_addr[0:1] == r"/":
        if ip_addr == r"/h" or ip_addr == r"/?":
                    print("Enter an ip address after iptobin.  Example iptobin 192.168.1.1")
                    exit(0)
        elif ip_addr == r"/a":
                    print("IP to binnary converter by Mike Ransom")
                    exit(0)
        else:
                    print("Valid options are ? -h -? -a /h /? /a")
                    exit(0)

    if ip_addr[0:1] == "?":
        print("Valid options are ? -h -? -a /h /? /a")
        exit(0)

    print("You entered an IP of %s" % ip_addr)
    temp = ip_addr.split(".")
    for i in temp:
        if (not str(i).isdigit()) or len(temp) != 4  or int(i) > 255 or int(i) < 0:
            print("You did not enter a valid IP.  Example iptobin 192.168.1.1")
            exit(1)
        ot.append(bin(int(i))[2:])

    for i in ot:

        if len(i) < 8:
            count = 8 - len(i)
            while count > 0:
                zeros += "0"
                count -= 1
            ot[c] = zeros + i
            zeros = ""

        c += 1

    print("Your IP in binnary is %s" % ".".join(ot))




else:
    print("You entered an incorrect number of paramators.  iptobin [ip address]")


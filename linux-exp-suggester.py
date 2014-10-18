#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import platform
from optparse import OptionParser

h00lyshit = {
    'Name': 'h00lyshit',
    'Kernel': [
        '2.6.8',  '2.6.10', '2.6.11', '2.6.12',
        '2.6.13', '2.6.14', '2.6.15', '2.6.16',
    ],
    'CVE': '2006-3626',
    'Source': 'http://www.exploit-db.com/exploits/2013/',
}
elflbl = {
    'Name': 'elflbl',
    'Kernel': ['2.4.29'],
    'Source': 'http://www.exploit-db.com/exploits/744/',
}
krad3 = {
    'Name': 'krad3',
    'Kernel': ['2.6.5', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11'],
    'Source': 'http://exploit-db.com/exploits/1397/',
}

exploits = [h00lyshit, elflbl, krad3]


def get_exploits(kernel_version, is_partial):
    prog = re.compile(kernel_version)
    for exploit in exploits:
        if prog.search(str(exploit['Kernel'])):
            print '[+] ' + exploit['Name']
            print_exploit(exploit)


def print_exploit(exploit):
    for _ in exploit:
        if _ != 'Name':
            print '    ' + _ + ':  ' + str(exploit[_])


def get_kernel_version():
    uname = platform.uname()
    system = uname[0]
    if system == 'Linux':
        kernel_version = uname[2]
    else:
        kernel_version = ''
        print '[-] local system is {system}!'.format(system=system)
    return kernel_version


def main():
    parser = OptionParser()
    parser.add_option("-k", "--kernel_version",
                      dest="kernel_version", help="kernel version number eg. 2.6.8 or eg. 2.6")
    (options, args) = parser.parse_args()
    if options.kernel_version:
        kernel_version = options.kernel_version
    else:
        kernel_version = get_kernel_version()
    if re.match('\d+\.\d+\.\d+', kernel_version):
        is_partial = False
    else:
        is_partial = True

    print kernel_version
    print
    get_exploits(kernel_version, is_partial)

if __name__ == "__main__":
    main()

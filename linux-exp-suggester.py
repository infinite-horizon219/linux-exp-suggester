#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from optparse import OptionParser

h00lyshit = {
    'name': 'h00lyshit',
    'vuln': [
        '2.6.8',  '2.6.10', '2.6.11', '2.6.12',
        '2.6.13', '2.6.14', '2.6.15', '2.6.16',
    ],
    'cve': '2006-3626',
    'refer': 'http://www.exploit-db.com/exploits/2013/',
}
elflbl = {
    'name': 'elflbl',
    'vuln': ['2.4.29'],
    'mil': 'http://www.exploit-db.com/exploits/744/',
}
krad3 = {
    'name': 'krad3',
    'vuln': ['2.6.5', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11'],
    'mil': 'http://exploit-db.com/exploits/1397',
}

exploits = [h00lyshit, elflbl, krad3]


def get_exploits(kernel_version):
    for exploit in exploits:
        if kernel_version in exploit['vuln']:
            print_exploit(exploit)
            print


def print_exploit(exploit):
    for _ in exploit:
        print _ + ':  ' + str(exploit[_])


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
                      dest="kernel_version", help="kernel version number eg.2.6.8")
    (options, args) = parser.parse_args()
    if options.kernel_version:
        kernel_version = options.kernel_version
    else:
        kernel_version = get_kernel_version()
    print kernel_version
    print
    get_exploits(kernel_version)

if __name__ == "__main__":
    main()

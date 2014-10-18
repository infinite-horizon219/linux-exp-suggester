linux-exp-suggester
--------
linux exploits suggester

## Usage

    linux-exp-suggester.py [options]

    Options:
    -h, --help            show this help message and exit
    -k KERNEL_VERSION, --kernel_version=KERNEL_VERSION kernel version number eg. 2.6.8 or eg. 2.6
    --download            download match exploits

## Example

    python linux-exp-suggester.py -k 2.6

    [+] h00lyshit
        Kernel:  ['2.6.8', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16']
        CVE:  2006-3626
        Source:  http://www.exploit-db.com/exploits/2013/
    [+] krad3
        Kernel:  ['2.6.5', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11']


    python linux-exp-suggester.py -k 2.6.16

    [+] h00lyshit
        Kernel:  ['2.6.8', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16']
        CVE:  2006-3626
        Source:  http://www.exploit-db.com/exploits/2013/


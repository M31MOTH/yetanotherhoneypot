#!/usr/bin/env python2
import sys
import optparse
from core.misc import printt
from core.config import user_agent as usera

def main():
    parser = optparse.OptionParser()
    options,r = parser.parse_args()

    from core.shell import shell
    shell()

if __name__ == '__main__':
    main()

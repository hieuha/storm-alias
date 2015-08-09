#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HieuHT --<>
  Purpose: 
  Created: 08/09/2015
"""
import optparse
import sys

def build_parser():
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage= usage)
    parser.add_option("-p", "--port", dest="port", help="2106", type="int", default=2106)
    parser.add_option("-d", "--debug", dest="debug", help="True|False", default=False)
    return parser

def main():
    from alias import web as web_service
    parser = build_parser()
    options, _args = parser.parse_args()        
    if options.debug:
        options.debug = True
    web_service.run(options.port, options.debug)

if __name__ == '__main__':
    main()
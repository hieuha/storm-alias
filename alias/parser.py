#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HieuHT --<>
  Purpose: Alias Parsers
  Created: 08/09/2015
"""
import re
from os.path import exists
from os.path import dirname
from os.path import expanduser
HOME = expanduser("~")

########################################################################
class Parser():
    """"""
    #----------------------------------------------------------------------
    def __init__(self, shell_profile = '.aliases'):
        """Constructor"""
        self.profile = HOME + '/' + shell_profile
        
    def read_profile(self):
        content_profile = ""
        if exists(self.profile):        
            with open(self.profile, 'r') as f:
                for line in f:            
                    line = line.strip()
                    content_profile += line + '\n'
                return content_profile
        else:
            print 'Profile Not Found!'
        return content_profile.strip()        

    def _parse_alias(self, line):
        re_line = re.search(r'(.*)[\s=\s]"(.*)"', line)
        if None != re_line:
            alias, command = re_line.groups()
            return alias, command

    def get_aliases(self, content_profile):
        aliases = []
        re_aliases = re.findall(r'(.*)alias[\s](.*)', content_profile)

        for line in re_aliases:
            _status, _line = line[0].strip(), self._parse_alias(line[1].strip())
            alias, command = _line        
            if '#' == _status:
                _line = (alias, (command, 0))
            else:
                _line = (alias, (command, 1))
            aliases.append(_line)
        return dict(aliases)
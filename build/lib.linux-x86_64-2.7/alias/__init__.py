#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HieuHT --<>
  Purpose: Storm Alias
  Created: 08/09/2015
"""
from os.path import expanduser
from os.path import exists
from parser import Parser
HOME = expanduser("~")

########################################################################
class Alias:
    """"""
    #----------------------------------------------------------------------
    def __init__(self, shell_profile = '.aliases'):
        """Constructor"""
        p = Parser(shell_profile)
        content_profile = p.read_profile()
        self.aliases = p.get_aliases(content_profile)
        self.gen()
    #----------------------------------------------------------------------    
    def get(self, alias):
        if self.aliases.has_key(alias):
            return self.aliases.get(alias)
    #----------------------------------------------------------------------
    def update(self, alias, command, status):
        self.aliases.update({alias: (command, status)})
        return self.gen()
    #----------------------------------------------------------------------
    def delete(self, alias):
        if self.aliases.has_key(alias):
            self.aliases.pop(alias, None)
            return self.gen()
    #----------------------------------------------------------------------    
    def item_to_string(self, item):        
        alias, _command = item
        command, status = _command
        if status == 1:
            return 'alias %s="%s"\n' % (alias, command)
        else:
            return '%s alias %s="%s"\n' % ('#', alias, command)
        
    def item(self, item):
        alias, _command = item
        command, status = _command
        item = {'name': alias,
                     'command': command,
                     'status': status}
        return item
    
    def list_entries(self, status = None):
        alias = []        
        for i in self.aliases.items():
            alias.append(self.item(i))
        self.gen()    
        return alias    
    
    #----------------------------------------------------------------------
    def gen(self, file_name = '.aliases'):
        """"""
        gen_file = HOME + '/' + file_name
        f = open(gen_file, 'w')
        for item in self.aliases.items():
            f.write(self.item_to_string(item))
        f.close()
    #----------------------------------------------------------------------       
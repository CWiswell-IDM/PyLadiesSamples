import ConfigParser
import os.path as path
import sys

configFilename = 'harness.ini'

if not path.exists(configFilename):
    print "Could not find config file {cf}".format(cf=configFilename)
    sys.exit(1)

cfg = ConfigParser.ConfigParser()
cfg.read(configFilename)
sections = cfg.sections()

active_section = 'ACTIVE'

if active_section not in sections:
    print "{sec} section not found in config file {cf}".format(sec=active_section,
                                                               cf=configFilename)
    sys.exit(1)

current_section = cfg.get(active_section, "environment")
if current_section not in sections:
    print "Section {cur} not found in config file {cf}".format(cur=current_section,
                                                               cf=configFilename)

username = cfg.get(active_section, "username")
password = cfg.get(active_section, "password")
endpoint = cfg.get(current_section, "modeling_url")
thread_count = cfg.getint(current_section, "thread_count")

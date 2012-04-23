# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser
from os import path
import sys

def fail(msg=None):
    if msg is not None:
        print msg
        print
    print """Make sure that the following Mercurial extensions are enabled:
 * mq [hgext.mq] (Mercurial patch Queues)
 * forest (Mercurial forest extension)
Also make sure that Mercurial uses the git diff format:
[diff]
nodates=1
git=1"""
    sys.exit(1)

if __name__ == '__main__':
    config = ConfigParser()
    if not config.read(path.expanduser('~/.hgrc')):
        fail()
    try:
        assert config.has_section('extensions'), "No extensions defined."
        assert config.has_section('diff'), "No diff settings defined."
        assert config.has_option('extensions', 'forest'), "Forest extension not enabled."
        assert config.has_option('extensions', 'hgext.mq'), "Patch Queue extension not enabled."
        assert config.has_option('diff','nodates'), "nodates=1 in [diff] not defined"
        assert config.has_option('diff','git'), "git=1 in [diff] not defined"
        assert config.getboolean('diff','nodates'), "nodates=1 in [diff] not defined"
        assert config.getboolean('diff','git'), "git=1 in [diff] not defined"
    except AssertionError, err:
        fail(err)

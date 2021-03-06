#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Transcoding watchfolder called EncodeBox
# Retrieved from git clone https://bitbucket.org/cloudncode/encodebox.git
u"""
    An example API only for debugging purposes.

    See http://celery.readthedocs.org/en/latest/configuration.html for a list of the available options.

    :author: David Fischer <david.fischer.ch@gmail.com>
    :copyright: (c) 2014 CloudNcode Inc. All rights reserved.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import pprint, requests

if __name__ == u'__main__':
    pprint.pprint(requests.get(u'http://127.0.0.1:5000/encoding/report').json())

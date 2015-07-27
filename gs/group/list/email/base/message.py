# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import (absolute_import, unicode_literals, print_function)
from email.mime.multipart import MIMEMultipart
from zope.cachedescriptors.property import Lazy
from zope.component import getGlobalSiteManager
from gs.group.base import GroupPage
from .interfaces import IMessagePart


class Message(GroupPage):

    @Lazy
    def parts(self):
        gsm = getGlobalSiteManager()
        retval = [a for a in gsm.getAdapters((self.context, self.request),
                                             IMessagePart)]
        retval.sort(key=lambda r: r[1].weight)
        return retval

    def __call__(self, *args, **kwargs):
        msg = self.as_email()
        retval = msg.as_string()
        return retval

    def as_email(self):
        retval = MIMEMultipart('alternative')
        for name, part in self.parts:
            p = part.as_email()
            retval.attach(p)
        return retval

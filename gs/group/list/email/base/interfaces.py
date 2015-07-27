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
from __future__ import absolute_import, unicode_literals
from zope.interface import Interface
from zope.schema import Int


class IPost(Interface):
    'A marker interface for a post'


class IMessage(Interface):
    def as_email():  # lint:ok
        '''The message as an instance of the :class:`email.message.Message` class'''


class IMessagePart(IMessage):
    weight = Int(
        title='Weight',
        description='The message parts are ordered by their weight, with the '
                    'simpler parts having smaller weights.',
        required=True)

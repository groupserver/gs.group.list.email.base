# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
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
from zope.component import getMultiAdapter
from gs.group.base import GroupPage
from .post import Post


class MessageTraversal(GroupPage):
    '''The "traversal" system for previewing messages

:param messages: The messages folder for a group.
:type messages: Products.XWFMailingListManager.interfaces.IGSMessagesFolder
:param request: The request-object.

It is useful to be able to preview messages. This class provides a way
of doing that: given a url of the form ``{postId}/{format}`` it loads
the post, and then returns the rendered version of the post in the correct
format.'''
    def __init__(self, messages, request):
        super(MessageTraversal, self).__init__(messages, request)
        self.traverse_subpath = []
        self.post = None

    def publishTraverse(self, request, name):
        '''Traverse through the path

The first time this method is called it loads the post referenced by
``name``. Subsequent calls just append ``name`` to the ``traverse_subpath``
property.'''
        self.traverse_subpath.append(name)
        if self.post is None:
            # Load the post, and hook it into the aquisition tree
            self.post = Post(self.context, self.groupInfo, name)
        return self

    def __call__(self):
        '''The traversal is done, render something.

Get a named adapter for the post, and the request, defaulting to the
``text`` name. Call the adapter, returning the result.'''
        tsp = self.traverse_subpath
        name = tsp[1] if len(tsp) > 1 else 'text'
        page = getMultiAdapter((self.post, self.request),
                               name=name)
        retval = page()
        return retval
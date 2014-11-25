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
from mock import patch, MagicMock
from unittest import TestCase
from gs.group.list.email.text.post import Post


class TestPost(TestCase):
    'Test the Post class'

    @patch.object(Post, 'post')
    def test_files(self, mock_post):
        gi = MagicMock()
        u = 'https://groups.example.com/groups/faux'
        gi.url.return_value = u

        files = [
            {'file_id': 'file0', 'file_name': 'dirk.txt',
             'file_size': 1023, 'mime_type': 'text/plain', },
            {'file_id': 'file1', 'file_name': 'dirk.html',
             'file_size': 2047, 'mime_type': 'text/html', }, ]
        mock_post.return_value = {
            'body': 'False post body',
            'files_metadata': files,
        }

        p = Post(gi, 'notAPostId')
        r = p.files

        for f in r:
            self.assertIn(u, f.url)
            self.assertIn('kb', f.size)

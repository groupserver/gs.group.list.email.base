============================
``gs.group.list.email.base``
============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The messages from a GroupServer group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-07-28
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

.. _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

The email messages that GroupServer_ sends from a group are
different from what is received. This product supplies the core
code for making that transformation. 

The message itself is formatted by ``gs.group.list.email.html``
[#html]_ and ``gs.group.list.email.text`` [#text]_.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.list.email.base
- Documentation: See the ``docs`` folder in this product
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

.. [#html] See the ``gs.group.list.email.html`` product
           <https://github.com/groupserver/gs.group.list.email.html>

.. [#text] See the ``gs.group.list.email.text`` product
           <https://github.com/groupserver/gs.group.list.email.text>

..  LocalWords:  IAppendix viewlets groupserver EmailTextPrologue

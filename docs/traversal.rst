Post traversal
==============

.. currentmodule:: gs.group.list.email.base.traverse

A *traversal* class is provided by this product. The main thing
that it provides is a way of previewing a post, either as `a
single message`_ or separately_.

.. _a single message:

Previewing a single message
---------------------------

To preview a single email message visit ``gs-group-list-email``
within the ``messages`` folder of a group, specifying the
post-identifier for the message.

.. code-block:: none

  http://groupserver.org/groups/development/messages/gs-group-list-email/{postId}

The *page* provided by the :class:`MessageTraversal` class loads
the post specified by the ``postId`` and then instantiates the
:class:`message.Message` class to :ref:`join the parts <join the
parts>` and return the single (ASCII) document.

.. _separately:

Previewing separate parts
-------------------------

The :class:`MessageTraversal` class can also preview the parts
separately if 

* The :ref:`part contents <part contents>` are specified as a
  browser *page*,
* The ``name`` of the part is specified in the URL, after the
  ``postId``

  .. code-block:: none

     …/gs-group-list-email/{postId}/{name}

Message traversal class
-----------------------

.. autoclass:: MessageTraversal

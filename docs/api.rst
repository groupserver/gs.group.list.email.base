:mod:`gs.group.list.email.base` API Reference
=============================================

.. currentmodule:: gs.group.list.email.base

The main API is provided by the `Post`_ class, which in turn
relies heavily on the `Queries`_ that marshal data from the
relational database. The API is also partly provided by
interfaces_.

Post
----

The :class:`Post` class takes a ``messages`` folder, the group
info, and a post-identifier and returns a representation of a
post that conforms with the :class:`interfaces.IPost` interface.

An instance of the :class:`Post` class is provided as the
*context* by the :doc:`traversal <traversal>` subsystem, and so
is used when creating a *page* that creates the :ref:`part
contents <part contents>`.

.. code-block:: python

  post = Post(groupInfo.groupObj.messages, groupInfo, postId)


.. autoclass:: Post

   .. data:: post

      The post as returned by :class:`queries.MessageQuery`

   .. data:: body

      The plain-text body of the post

   .. data:: files

      A list of files attached to the post. The elements of the
      list are instances of the :class:`post.File` class.

.. autoclass:: gs.group.list.email.base.post.File
   :members:


Queries
-------

.. currentmodule:: gs.group.list.email.base.queries

Most will never have to deal with the low-level
:class:`MessageQuery` class.

.. autoclass:: MessageQuery
   :members:

Interfaces
----------

.. currentmodule:: gs.group.list.email.base.interfaces

There are three interfaces provided by this product. The
:class:`IPost` interface is a marker interface, provided by the
:class:`gs.group.list.email.base.Post` class, while the `message
interfaces`_ are true interfaces.

.. autoclass:: IPost
   :members:

Message interfaces
~~~~~~~~~~~~~~~~~~

The two message interfaces, :class:`IMessage` and
:class:`IMessagePart`, are true interfaces: abstract base-classes
where all methods and properties are abstract (they also inherit
from :class:`zope.interface.Interface`). The former is provided
by the core message while the latter is provided by the different
parts of the message (see :doc:`parts`).

.. autoclass:: IMessage
   :members:

   .. method:: as_email()

      Return the post as an email message

      :returns: The post as an instance of the standard core
                email message class
      :rtype: :class:`email.message.Message`

.. autoclass:: IMessagePart
   :members:

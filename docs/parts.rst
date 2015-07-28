Creating message-parts
======================

.. currentmodule:: gs.group.list.email.base

The main use of the :mod:`gs.group.list.email.base` product is to
create parts of email messages. An email is rarely one document:
normally it is multiple documents in different formats. These
parts are joined together and sent out as one email. The
receiving email client decides which one to view, usually
selecting the most complex part that can be rendered (see
:rfc:`2046#section-5.1.4`).

In this section I will discuss the `anatomy of a part`_ and what
is required to `join the parts`_.

Anatomy of a part
-----------------

The main component of a message part is the `part adaptor`_,
which is usually declared separately from the `part contents`_.

Part adaptor
~~~~~~~~~~~~

A part of an email message implements the
:class:`interfaces.IMessagePart` interface. This is normally
declared in the ZCML for a product.

.. code-block:: xml

  <class class=".message.HTMLMessagePart">
    <implements
      interface="gs.group.list.email.base.interfaces.IMessagePart" />
  </class>

A part also adapts a post (:class:`interfaces.IPost`) and a
browser request
(:class:`zope.publisher.interfaces.browser.IBrowserRequest`),
providing the :class:`interfaces.IMessagePart`
interface. **Named** adaptors are used for the parts, because
there are multiple parts (adaptors) for a single post.

.. code-block:: xml

  <adapter
    name="html"
    for="gs.group.list.email.base.interfaces.IPost
         zope.publisher.interfaces.browser.IBrowserRequest"
    provides="gs.group.list.email.base.interfaces.IMessagePart"
    factory=".message.HTMLMessagePart" />

The part itself is required to supply a ``weight`` property, and
a ``to_email`` method:

``weight``:

  The ``weight`` is an integer that determines the order that the
  parts will be placed in the final document. Simple formats
  should be given small weights, with more complex formats higher
  values.

``to_email()``:

  The part as an :class:`email.message.Message` instance, or more
  likely a subclass from the :mod:`email.mime` module.

By using a separate class to generate the `part contents`_ the
implementation ofthe :meth:`.interfaces.IMessage.to_email` method
becomes fairly simple.

.. code-block:: python
   :linenos:

   htmlMessage = getMultiAdapter((self.context, self.request), name="html")
   html = htmlMessage()
   retval = MIMEText(html, 'html', 'utf-8')
   return retval

An instance class that generates the contents is created using
:func:`zope.component.getMultiAdapter`, with the contents itself
generated in the second. The contents is then added to a email
message subclass (:class:`email.mime.text.MIMEText`) before being
returned.

.. _part contents:

Part contents
~~~~~~~~~~~~~

It is convenient to generate the part contents in a completely
different class from the `part adaptor`_, as it allows the
contents of the one part to be examined separately from the
others (see :ref:`separately`).

The contents of a part can be declared as a standard Zope browser
*page,* using a post (:class:`interfaces.IPost`) as its context.

.. code-block:: xml

  <browser:page
    name="html"
    for="gs.group.list.email.base.interfaces.IPost"
    class=".message.HTMLMessage"
    template="browser/templates/page.pt"
    permission="zope2.View" />

This page, in turn, may be comprised of many viewlets that
actually generate the content.


.. _join the parts:

Joining the parts together
--------------------------

The parts are joined together by the :class:`.message.Message`
class. It adapts a post, as its context, and a browser
request. It then generates the :class:`interfaces.IMessagePart`
adaptors, using the same post and request. These adaptors are
then sorted (by ``weight``). A
:class:`email.mime.multipart.MIMEMultipart` email message is then
created (:mimetype:`multipart/alternative`) and each part is
added to the main message.

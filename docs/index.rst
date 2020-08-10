.. 从 BS4 迁移到 lxml 指南 documentation master file, created by
   sphinx-quickstart on Fri Mar 20 10:47:28 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

从 BS4 迁移到 lxml 指南！
===================================================

.. warning::
   本指南的所有内容仅在 Python 3 下通过测试，不保证在 Python 2 下依然可行！

术语标准
------------

在继续阅读本指南之前，我们应该建立一个关于 HTML 基本术语的共识，一般来说：

.. figure:: https://mdn.mozillademos.org/files/16475/element.png
  :alt: MDN element
.. figure:: https://mdn.mozillademos.org/files/16476/attribute.png
  :alt: MDN attribute

  以上图片引用自 `MDN`_

----

使用以下 HTML 代码生成 ``bs4.BeautifulSoup`` 对象和 ``lxml.etree._Element`` 对象::

    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    from lxml import etree
    ehtml = etree.HTML(html_doc)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   docs
   xpath

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _MDN: https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics

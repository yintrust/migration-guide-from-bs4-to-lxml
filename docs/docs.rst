lxml 补充文档
=====================

和之前类似，使用以下 HTML 代码生成 ``lxml.etree._Element`` 对象::

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

查找某个标签下的所有文本内容
----------------------------------

要查找某个标签下 **第一个子元素之前** 的文本内容，可使用 ``text`` 属性::

    p = ehtml.xpath('//p[@class="story"]')[0]
    p.text

这将打印出::

    Once upon a time there were three little sisters; and their names were

注意：``p`` 标签下的子标签，如 ``a`` 标签中的文本内容，以及第一个 ``a`` 标签之后的文本内容，将不会被打印出，
要包含其下的所有子标签中的文本内容，可使用 ``itertext()`` 方法::

    p = ehtml.xpath('//p[@class="story"]')[0]
    for i in p.itertext():
        print(i)

这将打印出::

    Once upon a time there were three little sisters; and their names were

    Elsie
    ,

    Lacie
     and

    Tillie
    ;
    and they lived at the bottom of a well.

查找某个属性的值
--------------------

使用 ``get()`` 方法即可::

    a = ehtml.xpath('//a[@class="sister"]')[0]
    a.get('href')

这将打印出::

    http://example.com/elsie

为某个属性设置新值
------------------

使用 ``set()`` 方法即可::

    a = ehtml.xpath('//a[@class="sister"]')[0]
    a.set('href', 'https://www.yintrust.com')

这将把第一个 ``a`` 标签的 ``href`` 属性的值设为 https://www.yintrust.com。

查找 **子** 元素
--------------------

在当前元素中通过标签名查找 **第一个** 匹配的 **子** 元素，可使用 ``find()`` 方法::

    p = ehtml.xpath('//p[@class="story"]')[0]
    p.find('a')

这将打印出第一个 ``a`` 元素；

在当前元素中通过标签名查找 **所有** 匹配的 **子** 元素，可使用 ``findall()`` 方法::

    p = ehtml.xpath('//p[@class="story"]')[0]
    p.findall('a')

这将返回一个列表，其中包含所有的 ``a`` 元素。

去除 HTML 中的所有标签
-------------------------

使用 ``lxml.html.HtmlElement`` 中的 ``text_content()`` 方法即可::

    from lxml import html
    document = html.document_fromstring(html_doc)
    document.text_content()

生成 ``lxml.etree._Element`` 对象的字符串
---------------------------------------------------

使用 ``lxml.etree`` 中的 ``tostring()`` 方法即可::

    etree.tostring(ehtml, encoding=str)

默认情况下返回 ``bytes`` 类型，指定 ``encoding=str`` 可使其返回 ``str`` 类型。

----

有关更多内容，可参考 lxml 的相关 API 文档：

- `lxml.etree API 文档`_
- `lxml.etree._Element API 文档`_
- `lxml.html.HtmlElement API 文档`_

.. _lxml.etree API 文档: https://lxml.de/api/lxml.etree-module.html
.. _lxml.etree._Element API 文档: https://lxml.de/api/lxml.etree._Element-class.html
.. _lxml.html.HtmlElement API 文档: https://lxml.de/api/lxml.html.HtmlElement-class.html

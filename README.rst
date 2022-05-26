Introduction
============

This addon register Galleria_ JQuery plugin in Plone's resource registries.

version: 1.6.1

About Galleria
==============

Galleria is a JavaScript image gallery framework built on top of the jQuery
library. The aim is to simplify the process of creating professional image
galleries for the web and mobile devices.


Requirements
============

- Plone 5.2 (tested)
- Python 3.6+, 2.7 (tested)


How to install
==============

.. image:: https://secure.travis-ci.org/collective/collective.js.galleria.png
    :target: http://travis-ci.org/collective/collective.js.galleria


To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add ``collective.js.galleria`` to the list of eggs to install:

.. code-block:: ini

    [buildout]
    ...
    eggs =
        collective.js.galleria

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.js.galleria`` and click the 'Activate' button.


Have an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.js.galleria/issues

Notes
=====

Galleria in its way to manage theme parse all link tags to find the css attached
to the theme. To make it work in production mode you must add themes javascript
and css called by the template. 
::

    // Patch for Plone
    // Escapes \+\+ from the urls \+\+resource\+\+, \+\+plone\+\+ and \+\+theme\+\+
    // to avoid errors in RegExp.
    _fix_plone_resource_url = (function(url) {
        return url.replace('\+\+plone\+\+', '\\+\\+plone\\+\\+').replace(
            '\+\+resource\+\+', '\\+\\+resource\\+\\+').replace(
                '\+\+theme\+\+', '\\+\\+theme\\+\\+')
    });

    ...

    // look for manually added CSS
    $('link').each(function( i, link ) {
        // Patch for Plone
        reg = new RegExp( _fix_plone_resource_url(theme.css) );
        if ( reg.test( link.href ) ) {

            // we found the css
            css = true;

            // the themeload trigger
            _themeLoad( theme );

            return false;
        }
    });


As you can see the original code has been patched to support ++resource++, ++plone++ and ++theme++ URLs.

Starting from version 1.6.1 this package is compatible only with Plone 5.2


Uglify Javascript
=================

To uglify Javascript, we can use the following commands:

.. code-block:: bash

    $ cd src/collective/js/galleria/resources
    $ yarn install
    $ yarn uglifyjs

This will generate ``galleria.min.js`` uglify based on ``galleria.js``.


Credits
=======

Companies
---------

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

Authors

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _galleria: https://galleriajs.github.io/ 

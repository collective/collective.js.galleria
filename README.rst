Introduction
============

This addon register Galleria_ JQuery plugin in Plone's resource registries.

version: 1.2.4

About Galleria
==============

Galleria is a JavaScript image gallery framework built on top of the jQuery
library. The aim is to simplify the process of creating professional image
galleries for the web and mobile devices.

Notes
=====

Galleria in its way to manage theme parse all link tags to find the css attached
to the theme. To make it work in production mode you must add themes javascript
and css called by the template. 
::

    // look for manually added CSS
    $('link').each(function( i, link ) {
        reg = new RegExp( theme.css.replace('\+\+resource\+\+','\\+\\+resource\\+\\+') );
        if ( reg.test( link.href ) ) {
            // we found the css
            css = true;
            Galleria.theme = theme;
            return false;
        }
    });

As you can see the original code has been patched to support ++resource++ url.


Credits
=======

Companies
---------

|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

Authors

  - JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. Contributors

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _galleria: http://galleria.aino.se
 

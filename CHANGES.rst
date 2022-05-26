Changelog
=========

1.6.3 (2022-05-26)
------------------

- Fix ``AttributeError`` when trying to create a Plone Site on an instance that has
  ``collective.js.galleria`` available.
  [wesleybl]


1.6.2 (2022-05-20)
------------------

- Allows using resources with ``++plone++`` in CSS definition URL of Galleria theme.
  [wesleybl]

- Use ``uglify-js`` node package to uglify Javascript.
  [wesleybl]

- Use plone resource instead of browser resource.
  [wesleybl]


1.6.1 (2022-02-07)
------------------

- Add support to Python 3.6, 3.7 and 3.8.
  [cleberjsantos]

- Add support to Plone 5.2.
  [cleberjsantos]

- Drop support for Plone 4.x
  [cleberjsantos]

- Update galleria to 1.6.1
  [clebejsantos]

- Add replacement for //resource// links for manually added css back in the
  1.6.1 galleria.js as written in the general notes (Based on changes in `0d2b832 <https://github.com/collective/collective.js.galleria/commit/0d2b8322ae90c0f746fd61a44c6164bc78b6c2d7#diff-7e954f54cc66afe1ef20acaf30599e1abba9bfde1c0bb92f25886b8eaa9d4db6>`_)  
  [cleberjsantos, fredvd]

- Add replacement in galleria.js for avoid error with jQuery load
  [cleberjsantos]


1.2.5 (2013-01-26)
------------------

- Add plugins as browser resources directory
  [cleberjsantos]
- Add travis-ci integration with test + python-validation
  [cleberjsantos][toutpt]

1.2.4 (2013-01-10)
------------------

- Update galleria to 1.2.9


1.2.3 (2012-08-15)
------------------

- Fix typo in previous release


1.2.2 (2012-08-15)
------------------

- Update galleria to 1.2.8


1.2.1 (2012-07-10)
------------------

- Fix CSS path to images loader and map.


1.2 (2012-04-05)
----------------

- upgrade to galleria 1.2.7


1.1 (2012-02-22)
----------------

- upgrade to galleria 1.2.6


1.0 (2012-01-04)
----------------

- Initial release

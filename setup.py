# -*- coding: utf-8 -*-
"""Installer for the collective.js.galleria package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.js.galleria",
    version="1.6.1",
    description="Register Galleria JQuery plugin in Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Python Plone CMS",
    author="JeanMichel FRANCOIS aka toutpt",
    author_email="toutpt@gmail.com",
    url="https://github.com/collective/collective.js.galleria",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.js.galleria",
        "Source": "https://github.com/collective/collective.js.galleria",
        "Tracker": "https://github.com/collective/collective.js.galleria/issues",
        # 'Documentation': 'https://collective.js.galleria.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.js"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*!=3.5.*",
    install_requires=[
        "setuptools",
        "plone.app.registry",
        "Products.CMFPlone>=5.2",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)

from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open(os.path.join("hexagonit", "portletroles", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("hexagonit", "portletroles", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("hexagonit", "portletroles", "docs", "CONTRIBUTORS.rst")).read()
)


setup(
    name='hexagonit.portletroles',
    version='1.0',
    description="Provides roles for adding each portlets.",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Hexagon IT',
    author_email='oss@hexagonit.fi',
    url='http://www.hexagonit.fi',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['hexagonit'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'hexagonit.testing',
        'plone.app.portlets',
        'plone.browserlayer',
        'setuptools',
        'z3c.autoinclude',
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)

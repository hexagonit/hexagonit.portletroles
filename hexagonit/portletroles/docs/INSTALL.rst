Installation
============

Use zc.buildout and the plone.recipe.zope2instance
recipe to manage your project:

* Add ``hexagonit.portletroles`` to the list of eggs::

    [buildout]
    ...
    eggs =
        ...
        hexagonit.portletroles

* Re-run buildout with::

    $ ./bin/buildout

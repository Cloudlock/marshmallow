********************************************
marshmallow2: simplified object serialization
********************************************

.. image:: https://badge.fury.io/py/marshmallow2.png
    :target: http://badge.fury.io/py/marshmallow2
    :alt: Latest version

.. image:: https://travis-ci.org/marshmallow2-code/marshmallow2.png?branch=pypi
    :target: https://travis-ci.org/marshmallow2-code/marshmallow2
    :alt: Travis-CI

Homepage: http://marshmallow2.readthedocs.org/

**marshmallow2** is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

.. code-block:: python

    from datetime import date
    from marshmallow2 import Schema, fields, pprint

    class ArtistSchema(Schema):
        name = fields.Str()

    class AlbumSchema(Schema):
        title = fields.Str()
        release_date = fields.Date()
        artist = fields.Nested(ArtistSchema)

    bowie = dict(name='David Bowie')
    album = dict(artist=bowie, title='Hunky Dory', release_date=date(1971, 12, 17))

    schema = AlbumSchema()
    result = schema.dump(album)
    pprint(result.data, indent=2)
    # { 'artist': {'name': 'David Bowie'},
    #   'release_date': '1971-12-17',
    #   'title': 'Hunky Dory'}


In short, marshmallow2 schemas can be used to:

- **Validate** input data.
- **Deserialize** input data to app-level objects.
- **Serialize** app-level objects to primitive Python types. The serialized objects can then be rendered to standard formats such as JSON for use in an HTTP API.

Get It Now
==========

::

    $ pip install -U marshmallow2


Documentation
=============

Full documentation is available at http://marshmallow2.readthedocs.org/ .

Requirements
============

- Python >= 2.6 or >= 3.3

marshmallow2 has no external dependencies outside of the Python standard library, although `python-dateutil <https://pypi.python.org/pypi/python-dateutil>`_ is recommended for robust datetime deserialization.

Project Links
=============

- Docs: http://marshmallow2.readthedocs.org/
- Changelog: http://marshmallow2.readthedocs.org/en/latest/changelog.html
- PyPI: https://pypi.python.org/pypi/marshmallow2
- Issues: https://github.com/marshmallow2-code/marshmallow2/issues


License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/marshmallow2-code/marshmallow2/blob/pypi/LICENSE>`_ file for more details.

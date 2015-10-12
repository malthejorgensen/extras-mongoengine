MongoEngine Extras
==================

The `extras-mongoengine` package provides the following extra fields for use on
MongoEngine `Document`s:

* `TimedeltaField` - a field for storing `datetime.timedelta` values.
* `LowerStringField` - a string field that transforms input strings to lowercase.
* `LowerEmailField` – a `LowerStringField` that also check if the string is valid according
   to the MongoEngine email regex (`EmailField.EMAIL_REGEX`).
* `IntEnumField` - a field for storing Python 3.4 (or later) [Enum values] where the values
  in the enum are `int`s.
* `StringEnumField` - a field for storing Python 3.4 (or later) [Enum values] where the values
  in the enum are `str`s.

[Enum values]: https://docs.python.org/3/library/enum.html

To use the `IntEnumField` and `StringEnumField` fields on Python 2.* or Python <3.4
you have to install the `enum34` package.

`StringEnumField` example
-------------------------

	from mongoengine import Document
	from enum import Enum
	from extras_mongoengine.fields import StringEnumField

	class BeverageType(Enum):
	    Tea = 'TEA'
	    Coffee = 'COFFEE'

	class Beverage(Document):
	    beverage_type = StringEnumField(BeverageType, default=BeverageType.Tea)

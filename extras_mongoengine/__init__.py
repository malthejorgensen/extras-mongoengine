try:
	import fields
except ImportError:
	# Python 3
	from . import fields

__all__ = ('fields')

class BarryFileException(Exception):
    """Raise exception when dealing with input files."""


class BarryConversionException(Exception):
    """Raise exception when converting file to dataframe."""


class BarryExportException(Exception):
    """Raise exception when writing dataframe to a file."""

class BarryDFException(Exception):
    """Raise exception while performing transformation to a dataframe."""

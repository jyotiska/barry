from exceptions import BarryFileException, BarryConversionException, BarryExportException
import pandas as pd


def detect_file_extension(filename):
    """Extract and return the extension of a file given a filename.

    Args:
        filename (str): name of the file
    Returns:
        str: extension of the file
    Raises:
        BarryFileException: if extension not present in filename
    """

    if filename is None:
        raise BarryFileException("Input file name cannot be None")

    split_filename = filename.split(".")

    if len(split_filename) > 1:
        return str(split_filename[-1]).lower()
    else:
        raise BarryFileException("Could not determine input file type from file extension")


def xls_to_df(filename, skip_rows, skip_header, columns):
    """Converts a XLS file to Pandas dataframe.

    Args:
        filename (str): name of the file
        skip_header (bool): whether to skip header
        columns (list or None): list of column names
    Returns:
        dataframe: a pandas dataframe
    Raises:
        BarryConversionException: if file cannot be converted to dataframe
    """

    try:
        # Check if columns names has been passed
        if columns is not None and len(columns) > 0:
            skip_header = 0

        # Check if header needs to be skipped
        if skip_header is True:
            skip_header = None
        else:
            skip_header = 0
        return pd.read_excel(filename, skiprows=skip_rows, header=skip_header, names=columns)
    except Exception as e:
        raise BarryConversionException("Could not convert file %s to dataframe" % (filename))


def xlsx_to_df(filename, skip_rows, skip_header, columns):
    """Converts a XLSX file to Pandas dataframe.

    Args:
        filename (str): name of the file
        skip_header (bool): whether to skip header
        columns (list or None): list of column names
    Returns:
        dataframe: a pandas dataframe
    Raises:
        BarryConversionException: if file cannot be converted to dataframe
    """

    try:
        # Check if columns names has been passed
        if columns is not None and len(columns) > 0:
            skip_header = 0

        # Check if header needs to be skipped
        if skip_header is True:
            skip_header = None
        else:
            skip_header = 0
        return pd.read_excel(filename, skiprows=skip_rows, header=skip_header, names=columns)
    except Exception as e:
        raise BarryConversionException("Could not convert file %s to dataframe" % (filename))


def csv_to_df(filename, skip_rows, skip_header, columns):
    """Converts a CSV file to Pandas dataframe.

    Args:
        filename (str): name of the file
        skip_header (bool): whether to skip header
        columns (list or None): list of column names
    Returns:
        dataframe: a pandas dataframe
    Raises:
        BarryConversionException: if file cannot be converted to dataframe
    """

    try:
        # Check if columns names has been passed
        if columns is not None and len(columns) > 0:
            skip_header = 0

        # Check if header needs to be skipped
        if skip_header is True:
            skip_header = None
        else:
            skip_header = 0
        return pd.read_csv(filename, skiprows=skip_rows, header=skip_header, names=columns)
    except Exception as e:
        raise BarryConversionException("Could not convert file %s to dataframe" % (filename))


def df_to_xls(df, out_filename):
    """Writes a Pandas dataframe to a XLS file.

    Args:
        df (dataframe): dataframe to be written to file
        filename (str): name of the file
    Raises:
        BarryExportException: if file cannot be converted to dataframe
    """

    try:
        df.to_excel(out_filename)
    except Exception as e:
        raise BarryExportException("Could not write dataframe to file %s" % (out_filename))


def df_to_xlsx(df, out_filename):
    """Writes a Pandas dataframe to a XLS file.

    Args:
        df (dataframe): dataframe to be written to file
        filename (str): name of the file
    Raises:
        BarryExportException: if file cannot be converted to dataframe
    """

    try:
        df.to_excel(out_filename)
    except Exception as e:
        raise BarryExportException("Could not write dataframe to file %s" % (out_filename))


def df_to_json(df, out_filename):
    """Writes a Pandas dataframe to a JSON file.

    Args:
        df (dataframe): dataframe to be written to file
        filename (str): name of the file
    Raises:
        BarryExportException: if file cannot be converted to dataframe
    """

    try:
        df.to_json(out_filename)
    except Exception as e:
        raise BarryExportException("Could not write dataframe to file %s" % (out_filename))


def df_to_csv(df, out_filename):
    """Writes a Pandas dataframe to a CSV file.

    Args:
        df (dataframe): dataframe to be written to file
        filename (str): name of the file
    Raises:
        BarryExportException: if file cannot be converted to dataframe
    """

    try:
        df.to_csv(out_filename)
    except Exception as e:
        raise BarryExportException("Could not write dataframe to file %s" % (out_filename))

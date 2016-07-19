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


def xls_to_df(filename):
    """Converts a XLS file to Pandas dataframe.

    Args:
        filename (str): name of the file
    Returns:
        dataframe: a pandas dataframe
    Raises:
        BarryConversionException: if file cannot be converted to dataframe
    """

    try:
        return pd.read_excel(filename)
    except Exception as e:
        raise BarryConversionException("Could not convert file %s to dataframe" % (filename))


def xlsx_to_df(filename):
    """Converts a XLSX file to Pandas dataframe.

    Args:
        filename (str): name of the file
    Returns:
        dataframe: a pandas dataframe
    Raises:
        BarryConversionException: if file cannot be converted to dataframe
    """

    try:
        return pd.read_excel(filename)
    except Exception as e:
        raise BarryConversionException("Could not convert file %s to dataframe" % (filename))


def csv_to_df(filename):
    """Converts a CSV file to Pandas dataframe.

    Args:
        filename (str): name of the file
    Returns:
        dataframe: a pandas dataframe
    Raises:
        BarryConversionException: if file cannot be converted to dataframe
    """

    try:
        return pd.read_csv(filename)
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

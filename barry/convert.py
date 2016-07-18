from exceptions import BarryFileException
import pandas as pd

def detect_file_extension(filename):
    if filename is None:
        raise BarryFileException("Input file name cannot be None")

    split_filename = filename.split(".")

    if len(split_filename) > 1:
        return str(split_filename[-1]).lower()
    else:
        raise BarryFileException("Could not determine input file type from file extension")


def xls_to_df(filename):
    return pd.read_excel(filename)


def xlsx_to_df(filename):
    return pd.read_excel(filename)


def csv_to_df(filename):
    return pd.read_csv(filename)


def df_to_xls(df, out_filename):
    df.to_excel(out_filename)


def df_to_xlsx(df, out_filename):
    df.to_excel(out_filename)


def df_to_json(df, out_filename):
    df.to_json(out_filename)


def df_to_csv(df, out_filename):
    df.to_csv(out_filename)

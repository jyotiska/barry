import pandas as pd
import sys

from utils import get_options
from exceptions import BarryFileException
import convert


def main():
    """Entry point of the program."""

    # Get all command line arguments
    cmd_options = vars(get_options())

    # Determine the extension of the input file
    input_file_extension = convert.detect_file_extension(cmd_options["in_filename"])

    # Initialize the empty dataframe
    df = None

    # Check if rows need to be skipped from start
    skip_rows = int(cmd_options["skip_rows"])

    # Check if the user wants to skip header
    skip_header = cmd_options["skip_header"]

    # Check if the user has passed a list of columns names explicitly
    column_names = cmd_options["columns"]
    if column_names is not None:
        column_names = column_names.split(",")

    # Based on extension, convert the file contents to a Pandas dataframe
    if input_file_extension == "xls":
        df = convert.xls_to_df(cmd_options["in_filename"], skip_rows, skip_header, column_names)
    elif input_file_extension == "xlsx":
        df = convert.xlsx_to_df(cmd_options["in_filename"], skip_rows, skip_header, column_names)
    elif input_file_extension == "csv":
        df = convert.csv_to_df(cmd_options["in_filename"], skip_rows, skip_header, column_names)
    else:
        raise BarryFileException("Input file format not supported. Currently supported file formats - xls/xlsx/csv")

    # Based on the output format, write the dataframe to disk
    if cmd_options["out_format"] == "xls":
        convert.df_to_xls(df, cmd_options["out_filename"])
    elif cmd_options["out_format"] == "xlsx":
        convert.df_to_xlsx(df, cmd_options["out_filename"])
    elif cmd_options["out_format"] == "json":
        convert.df_to_json(df, cmd_options["out_filename"])
    else:
        convert.df_to_csv(df, cmd_options["out_filename"])


if __name__ == '__main__':
    main()

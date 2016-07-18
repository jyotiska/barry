import pandas as pd
import sys

from utils import get_options
from exceptions import BarryFileException
import convert

def main(argv):
    cmd_options = vars(get_options(argv))

    input_file_extension = convert.detect_file_extension(cmd_options["in_filename"])
    df = None

    if input_file_extension == "xls":
        df = convert.xls_to_df(cmd_options["in_filename"])
    elif input_file_extension == "xlsx":
        df = convert.xlsx_to_df(cmd_options["in_filename"])
    elif input_file_extension == "csv":
        df = convert.csv_to_df(cmd_options["in_filename"])
    else:
        raise BarryFileException("Input file format not supported. Currently supported file formats - xls/xlsx/csv")

    if cmd_options["out_format"] == "xls":
        convert.df_to_xls(df, cmd_options["out_filename"])
    elif cmd_options["out_format"] == "xlsx":
        convert.df_to_xlsx(df, cmd_options["out_filename"])
    elif cmd_options["out_format"] == "json":
        convert.df_to_json(df, cmd_options["out_filename"])
    else:
        convert.df_to_csv(df, cmd_options["out_filename"])

if __name__ == '__main__':
    main(sys.argv)

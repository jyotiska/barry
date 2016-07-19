from optparse import OptionParser

def get_options(argv):
    parser = OptionParser()
    parser.add_option("-i", "--input", default=None, dest="in_filename", help="Input File Name (Required)", metavar="<input_filename>")
    parser.add_option("-o", "--output", default=None, dest="out_filename", help="Output File Name (Required)", metavar="<output_filename>")
    parser.add_option("-f", "--format", default="csv", dest="out_format", help="Output File Format", metavar="json/csv/xls/xlsx/txt")
    parser.add_option("--skip-rows", default=0, dest="skip_rows", help="Number of rows to skip (Default 0)")
    parser.add_option("--skip-header", action="store_true", default=False, dest="skip_header", help="Skip column header (Default False)")
    parser.add_option("--delimiter", default=",", dest="delimiter", help="Delimiter to use for parsing (Default comma)")
    parser.add_option("-s", "--sort", default=None, dest="sort_column", help="Column name to sort (default None)", metavar="<sort_column_name>")
    parser.add_option("-r", "--rsort", default=None, dest="rsort_column", help="Column name to reverse sort (default None)", metavar="<rsort_column_name>")

    (options, args) = parser.parse_args()

    if not options.in_filename:   # if filename is not given
        parser.error('Input file name is required. Use -h for usage.')

    if not options.out_filename:
        parser.error("Output file name is required. Use -h for usage.")

    return options
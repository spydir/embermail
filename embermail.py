# !/usr/bin/env python
#

# import modules used here -- sys is a very standard one
import auth
import input_validation
import analyze
import sys, argparse, logging


# Gather our code in a main() function
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    # TODO Replace this with your actual code.


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Downloads gmail metatdata and does analysis")
    # TODO Specify your real parameters here.

    parser.add_argument(
        "-d",
        "--download",
        help="downloads email metadata",
        action="store_true")

    parser.add_argument(
        "-a",
        "--analyze",
        help="analyzes email metadata",
        action="store_true")

    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    args = parser.parse_args()

    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    if args.analyze:
        analyze.analyze("./emails")

    if args.download:
        # analyze.download_emails('emails/')
        analyze.inbox_unread('inbox/')

    main(args, loglevel)


#


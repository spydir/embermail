# !/usr/bin/env python
#

import analyze, argparse, logging
from utils import downloads

# Gather our code in a main() function
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    # TODO Replace this with your actual code.


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Downloads gmail metatdata and does analysis")
    # TODO Specify your real parameters here.

    parser.add_argument(
        "-iu",
        "--inboxunread",
        help="downloads unread email from the inbox",
        action="store_true")

    parser.add_argument(
        "-u",
        "--unread",
        help="downloads all unread email",
        action="store_true")

    parser.add_argument(
        "-i",
        "--inbox",
        help="downloads all inbox email",
        action="store_true")

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
        # analyze.analyze("./emails")
        analyze.comapare_dirs('./inbox/')

    if args.download:
        downloads.download('./all_mail/','all_mail')

    if args.inbox:
        downloads.download('./inbox/','inbox')

    if args.unread:
        downloads.download('./unread/', 'unread')

    if args.inboxunread:
        downloads.download('./inbox_unread/','inbox_unread')

    main(args, loglevel)

#
# if __name__ == '__main__':
#     downloads.download('./inbox/', 'inbox')


import argparse
import logging
import json
from importlib_resources import files
import os
import mypackage


def main():
    parser = argparse.ArgumentParser(description="Example CLI")
    parser.add_argument(
        "--loglevel",
        type=str,
        action="store",
        default="info",
        required=False,
        help="One of ['warning', 'info', 'error', 'debug', 'critical']",
    )
    args = parser.parse_args()
    logging.basicConfig(level=logging.getLevelName(args.loglevel.upper()))
    logging.info("Hi there")
    logging.info("Here is that JSON resource we packaged")
    source = files(mypackage).joinpath(
        os.path.join("data", "random_file.json"))
    with open(str(source)) as json_src:
        print(json.load(json_src))
    logging.info("Bye now")


if __name__ == "__main__":
    main()

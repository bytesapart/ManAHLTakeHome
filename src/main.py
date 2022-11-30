"""
Author: Osama Iqbal
"""

import sys
import logger
import randompick
import argparse
import math


def parse_args():
    """
    Parses the arguments given to the script
    Returns
    -------
    argparse.Namespace: A dictionary-like object containing the arguments passed
    """
    log.info("Starting parse_args() function")
    parser = argparse.ArgumentParser(description='Generate a random number based off of probabilities')
    parser.add_argument('-m', '--method', help='The method to use. The values are "naive", "efficient" or "alias"',
                        required=True, choices=['naive', 'efficient', 'alias'])
    parser.add_argument('-n', '--numbers', help='A comma separated list of numbers to choose from', required=True)
    parser.add_argument('-p', '--probabilities',
                        help='A comma separated list of probabilities to choose from. Must sum up to 1', required=True)
    if len(sys.argv) < 2:
        parser.print_help()
        parser.print_usage()

    log.info("End parse_args() function")
    return parser.parse_args()


def validate_args(args: argparse.Namespace):
    """
    Parameters
    ----------
    args: argparse.Namespace
        dictionary of arguments given to the script
    Returns
    -------
    None
    """
    log.info("Starting validate_args() function")
    if not math.isclose(sum([float(probability) for probability in args.probabilities.split(',')]), 1):
        raise ValueError("The probabilities provided to the script must be nearly equal to 1")

    if len(args.numbers.split(',')) != len(args.probabilities.split(',')):
        raise ValueError(
            "The numbers to select and the probabilities have a mismatch. Their numbers should be the same")
    log.info("End validate_args() function")

    if len(args.numbers) == 0:
        raise ValueError('Numbers must be a non-empty parameter')

    if len(args.probabilities) == 0:
        raise ValueError('Probabilities must be a non-empty parameter')


def sanitise_args(args: argparse.Namespace):
    """
    Sanitise the arguments given to the script.
    Parameters
    -------
    args: argparse.Namespace
        List of arguments that need to be sanitised
    Returns
    -------
    None
    """
    log.info("Starting sanitise_args() function")
    args.numbers = [float(number) for number in args.numbers.split(',')]
    args.probabilities = [float(probability) for probability in args.probabilities.split(',')]
    log.info("End sanitise_args() function")


def main():
    """
    The main function of the program containing the business logic
    Returns
    -------
    int: Returns 0 if program runs successfully, or returns 1
    """
    try:
        log.info("Starting main() function")
        # ===== Step 1: Get all the parameters from the console =====
        args = parse_args()
        validate_args(args)
        sanitise_args(args)

        # ===== Step 2: Process the business logic according to what the arguments are =====
        randomgen_obj = randompick.RandomGen(args.numbers, args.probabilities, args.method)
        random_number = [randomgen_obj.next_num() for i in range(100)]
        random_number_counts = {number: random_number.count(number) for number in args.numbers}
        print(f'Random Numbers for 100 iterations are {random_number_counts}')
        log.info(f'Random Numbers for 100 iterations are {random_number_counts}')

        log.info("End main() function")
    except Exception as error:
        log.exception(error)
    finally:
        logger.logging.shutdown()


if __name__ == '__main__':
    # Initialize the logger
    log = logger.init_logger()
    # Call the main function
    sys.exit(main())

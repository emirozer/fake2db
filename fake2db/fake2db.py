import argparse

parser = argparse.ArgumentParser(description='Create test databases that are '
                                             '  populated with fake data.')

parser.add_argument('amount_of_rows', metavar='-r', type=int, nargs='+',
                   help='amount of rows')

parser.add_argument('database_pattern', metavar='-p', type=str, nargs='+',
                   help='pattern of the database to be created')

parser.add_argument('target_db', metavar='-d', type=str, nargs='+',
                   help='target database / postgresql ? mysql ? sqlite ?')

args = parser.parse_args()

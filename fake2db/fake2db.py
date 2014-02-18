import argparse

parser = argparse.ArgumentParser(description='Create test databases that are populated with fake data.')

parser.add_argument('amount of rows', metavar='-r', type=int, nargs='+',
                   help='amount of rows')
parser.add_argument('database pattern', metavar='-p', type=str, nargs='+',
                   help='pattern of the database to be created')
parser.add_argument('target db', metavar='-d', type=int, nargs='+',
                   help='target database / redis ? mongodb ? mysql ? sqlite ?')

args = parser.parse_args()
print args.accumulate(args.integers)

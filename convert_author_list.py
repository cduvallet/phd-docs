""" 
Convert an author list with first name last name into
last name, F.I.
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('authors', help='Current list of authors')

args = parser.parse_args()
authors = args.authors

authors = [i.strip().split(' ') for i in authors.split(' and ')]
authors = [i[-1] + ', ' + '.'.join([i[j][0] for j in range(len(i)-1)]) + '.' for i in authors]
print('\n')
print(' and '.join(authors))


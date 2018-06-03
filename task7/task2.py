import argparse
import os.path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--year',
                    help='Displays Top250 movies titles with year',
                    action='store_true')
parser.add_argument('--rate',
                    help='Displays Top250 movies titles with rate',
                    action='store_true')
parser.add_argument('--all',
                    help='Shows title, rate, year',
                    action='store_true')
parser.add_argument('--histogram',
                    help='Displays histogram for rating or for '
                         'years (in text format)')
parser.add_argument('--output',
                    help='Stores data to specified filename file')
args = parser.parse_args()

filename = 'IMDB-Movie-Data.csv'
if os.path.exists(filename):
    df = pd.read_csv(filename)
    if args.year:
        sorted_df = df.sort_values(by=['Year', 'Title'],
                                   ascending=[False, True])[:250]
        result_df = sorted_df[['Title', 'Year']]
    if args.rate:
        sorted_df = df.sort_values(by=['Rating', 'Title'],
                                   ascending=[False, True])[:250]
        result_df = sorted_df[['Title', 'Rating']]
    if args.all:
        result_df = df[['Title', 'Rating', 'Year']]
    if args.histogram == 'rating':
        grouped_df = df.groupby('Rating')['Rating'].count()
        result_df = grouped_df.sort_index(ascending=False)
    if args.histogram == 'year':
        grouped_df = df.groupby('Year')['Year'].count()
        result_df = grouped_df.sort_index(ascending=False)
    if args.output:
        result_df.to_csv(args.output)
    else:
        print(result_df.to_string())
else:
    print('File doesn\'t exist!')

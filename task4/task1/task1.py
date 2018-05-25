import csv


def ratings_field(element):
    return element[2]


def sort_movies(movies_list):
    movies_list.sort(key=ratings_field, reverse=True)


def aggregate_movies(movies):
    result = {}
    for movie in movies:
        res = result.get(movie[1], [0, 0.0])
        res[0] += 1
        res[1] += float(movie[2])
        result[movie[1]] = res
    return result


# read file
all_movies = []
try:
    with open('task1/IMDB-Movie-Data.csv', 'r') as movies:
        reader = csv.DictReader(movies)
        for row in reader:
            all_movies.append([row["Title"], row["Year"], row["Rating"]])
except FileNotFoundError:
    print('File Not Found!')

# write top 250
sort_movies(all_movies)
with open('top250_movies.csv', 'w') as top250:
    writer = csv.writer(top250)
    for row in all_movies[:250]:
        writer.writerow([row[0]])

# write aggregations
aggregated_movies = {}
for k, v in aggregate_movies(all_movies).items():
    aggregated_movies[k] = v[1] / v[0]
with open('ratings.csv', 'w') as aggregated:
    writer = csv.writer(aggregated)
    for k, v in aggregated_movies.items():
        writer.writerow([k, v])

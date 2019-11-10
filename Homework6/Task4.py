# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле
#     ./data6/ ratings.list.
# Откройте и прочитайте файл(если его нет
#     необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt –
# названия файлов, ratings.txt – гистограмма
# рейтингов, years.txt – гистограмма годов.

try:
    ratings_list_reader = open('Homework6/data/ratings.list', 'r', encoding="ISO-8859-1")
except NameError:
    print('Error: This folder does not contain this file.')

films_list = []
for line in ratings_list_reader:
    if line.startswith('      000000'):
        films_list.append(line.strip())
        if len(films_list) == 250:
            break

films_list_upd = [el.split('  ') for el in films_list]

# data for top250_movies.txt
films_title = [el[-1] for el in films_list_upd]
films_title_upd = [el.split() for el in films_title]
films_title_upd2 = [el[:-6] for el in films_title]
films_title_funnaly = [el.strip() for el in films_title_upd2]

# data for years.txt
films_years = [el[-1].strip('()/I') for el in films_title_upd]
films_years = list(map(int, films_years))

# data for ratings.txt
films_ratings = [el[-2] for el in films_list_upd]
films_ratings = list(map(float, films_ratings))

with open('Homework6/data/top250_movies.txt', 'w') as top_250:
    text = '\n'.join(films_title_funnaly)
    top_250.write(text)
    top_250.close()

with open('Homework6/data/ratings.txt', 'w') as ratings:
    dct_ratings = {}
    for el in films_ratings:
        dct_ratings[el] = dct_ratings.get(el, 0) + 1
    for key, value in dct_ratings.items():
        ratings.write(str(key) + ' ' + int(value) * '+' + '\n')
    ratings.close()

with open('Homework6/data/years.txt', 'w') as years:
    dct_years = {}
    for el in films_years:
        dct_years[el] = dct_years.get(el, 0) + 1
    for key, value in dct_years.items():
        years.write(str(key) + ' ' + int(value) * '+' + '\n')
    years.close()

ratings_list_reader.close()

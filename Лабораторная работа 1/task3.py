# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
numbers_of_pages = 100
numbers_of_rows = 50
numbers_of_symbols = 25
one_symbol = 4

volume1 = volume * 1024 * 1024
count_symbols = numbers_of_symbols * numbers_of_rows * numbers_of_pages
volume_book = count_symbols * 4
count_books = volume1 // volume_book

print("Количество книг, помещающихся на дискету:", int(count_books))

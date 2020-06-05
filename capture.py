import urllib.request as url
from random import randrange
from numpy.random import randint
import sys
import os
import re

'''
Script captures books from www.gutenberg.org and transforms them to txt files.
Each book has unique identificator in form of an integer number so request looks
as below:
    http://www.gutenberg.org/files/book_id/book_id.txt
and in some cases:
    http://www.gutenberg.org/files/book_id/book_id-number.txt
where number is an integer 0-9. In some cases books with number throws exception during
utf-8 decoding which indicates that decoder met unknown sign(languages with their own signs)
or unknown formatting.
'''

def get_url_text_safe(url_loc,file_localisation):
    try:
        txt = url.urlopen(url_loc).read()
        if sys.getsizeof(txt) > 0:
            with open(file_localisation, 'w+') as out_file:
                out_file.write(txt.decode("utf-8"))
    except Exception as e:
        # print(f"Exc: {e}")
        if os.path.exists(file_localisation):
            os.remove(file_localisation)

N_books = 500
books_ids_range = 14000

gutenberg_books_ids = randint(books_ids_range, size = N_books)

for gutenberg_book_id in gutenberg_books_ids:
    print(gutenberg_book_id)

    try:
        url_req = f'http://www.gutenberg.org/files/{gutenberg_book_id}'
        book_file = url.urlopen(url_req).read()
        possinle_ids = []
        new_url = url_req + f"/{gutenberg_book_id}.txt"
        get_url_text_safe(new_url,f"data/{gutenberg_book_id}.txt")
        pattern = re.compile(f"-[0-9].txt") #the pattern actually creates duplicates in the list

        possinle_ids = pattern.findall(book_file.decode("utf-8"))
        for possinle_id in possinle_ids:
            get_url_text_safe(url_req + f"/{gutenberg_book_id}{possinle_id}",f"data/{gutenberg_book_id}{possinle_id}")

    except Exception as e:
        new_url = url_req + f"/{gutenberg_book_id}.txt"
        get_url_text_safe(new_url,f"data/{gutenberg_book_id}.txt")    
        # print(f"Exc: {e}") 
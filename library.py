import sqlite3 as sql
import requests as req
import json

# ISBN
url = "https://openlibrary.org/"

# Books
with open("isbn_list.txt", "r+") as f:
    isbnlist_object = f.read()

isbnlist = isbnlist_object.splitlines()
json_data_list = []
values_list = []
isbn = ""

# DB
con = sql.connect("books.db")
cur = con.cursor()
columns = "ISBN, title, authors, pages, published, revision, physical_format"
# _______________________ ISBN Request ________________________

for isbn in isbnlist:
    response = req.get(url + "isbn/" + isbn.strip() + ".json")
    json_data_list.append(json.loads(response.text))


# Get data from request
def get_data(data):
    authors_empty = True
    authorsdict = []
    title = ""
    authors = ""
    pages = 0
    published = ""
    revision = 0
    pformat = ""
    for key, value in data.items():
        if key == "title":
            title = value
        elif key == "authors":
            authorsdict = value
        elif key == "by_statement":
            if str(authorsdict) == "dict_values([])":
                authors_empty = not authors_empty
                authors = value
        elif key == "number_of_pages":
            pages = value
        elif key == "publish_date":
            published = value
        elif key == "revision":
            revision = value
        elif key == "physical_format":
            pformat = value

    # authors from list dictionary to names string
    if authors_empty:
        for item in authorsdict:
            for key, value in item.items():
                resp = req.get(url + value + ".json")
                data = json.loads(resp.text)
                for xkey, xvalue in data.items():
                    if xkey == "name":
                        authors += xvalue + ", "

    output = title + "', '" + authors + "', '" + str(pages) + "', '" + published + "', '" + str(revision) + "', '" + pformat + "'"
    return output


for json_data in json_data_list:
    values_list.append("'" + isbn + "', '" + get_data(json_data))

# _______________________ DB Functions ________________________
tableList = cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='books';""").fetchall()

if not tableList:
    cur.execute("CREATE TABLE books (" + columns + ")")

for values in values_list:
    cur.execute("INSERT INTO books (" + columns + """)
                VALUES(""" + values + ")")

cur.execute("SELECT * FROM books")
print(cur.fetchall())

import sqlite3 as sql
import requests as req
import json

# ISBN
url = "https://openlibrary.org/"

# Books
isbn = "1888996471"

# DB
con = sql.connect("books.db")
cur = con.cursor()
columns = "ISBN, title, authors, pages, published, revision, physical_format"
# _______________________ ISBN Request ________________________


response = req.get(url + "isbn/" + isbn + ".json")
json_data = json.loads(response.text)


# Get data from request
def get_data(data):
    authors_empty = True
    authorsdict = []
    title = ""
    authors = ""
    pages = ""
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

    return title, authors, pages, published, revision, pformat


values = get_data(json_data)

print(values)

#row = "'" + isbn + "', '" + title + "', '" + authors + "', '" + str(pages) + "', '" + published + "', '" + str(revision) + "', '" + pformat + "'"

# _______________________ DB Functions ________________________
#cur.execute("DROP TABLE books")
#cur.execute("CREATE TABLE books (" + columns + ")")
#cur.execute("INSERT INTO books (" + columns + """)
#           VALUES(""" + row + ")")
#cur.execute("SELECT * FROM books")
#print(cur.fetchall())

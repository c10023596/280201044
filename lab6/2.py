books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in range(len(books)):
  book_name = books[i]
  unq_letters = list(set(book_name))
  value = len(book_name),len(unq_letters)
  book_dict[book_name]=value
print(book_dict)
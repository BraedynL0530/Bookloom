
class Bookshelf:
    def __init__(self):
        self.books = [] #{id: name: author tags: desc: source:(epub, cbz, or web based viewing)}
        self.books_per_row = 10 # idk default
        self.order = None
        self.favorite = [] #ids
        self.current_rows = 1 #not visual editing rows but 4 layout(unless its over the image rows)


    def add_book(self, book):
        self.books.append(book)
        if self.books_per_row < len(self.books) // self.books_per_row:
            self.current_rows += 1

    def __len__(self):
        return len(self.books)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        if self.books_per_row > len(self.books) // self.books_per_row & self.books_per_row != 1 | self.books_per_row != 0:
            self.current_rows -= 1


    # TOD
    def search_book(self, book):
        for i in self.books:
            if i.title == book:
                return i # may need to fix this

    def get_books(self):
        return self.books

    def get_book(self, id):
        for i in self.books:
            if i.id == id:
                return i

    def reorder_books(self, books):
        return # ts should be like chapter ascending/de, or recents

    def set_books_per_row(self, books_per_row):
        self.books_per_row = books_per_row

    def add_favorite(self, id):
        self.favorite.append(id)

    def remove_favorite(self, id):
        self.favorite.remove(id)

class Bookshelf:
    def __init__(self):
        self.books = [] #{id: name: author tags: desc: source:(epub, cbz, or web based viewing)}
        self.books_per_row = 10 # idk default
        self.order = None
        self.favorite = [] #ids


    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)


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

    def set_row_count(self, row_count):
        self.row_count = row_count

    def set_books_per_row(self, books_per_row):
        self.books_per_row = books_per_row
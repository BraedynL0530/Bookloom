from uuid import UUID


class Bookshelf:
    def __init__(self):
        self.books = [] #list of ids Books class will have data 4 display
        self.books_per_row = 10 # idk default
        self.order = None
        self.favorite = [] #ids
        self.current_rows = 1 #not visual editing rows but 4 layout(unless its over the image rows)


    def add_book(self, book: UUID):
        self.books.append(book)
        self.update_shelf(book)


    def __len__(self):
        return len(self.books)

    def remove_book(self, book: UUID):
        if book in self.books:
            self.books.remove(book)
            self.update_shelf(book)

    def update_shelf(self, books:list):
        return
        #clac rows needed here
        #update current rows
        #other stuff




    def search_book(self, book:str) -> str: #title
        for i in self.books:
            if i.title == book:
                return i


    def reorder_books(self, books):
        return # ts should be like chapter ascending/de, or recents

    def set_books_per_row(self, books_per_row):
        self.books_per_row = books_per_row

    def add_favorite(self, id):
        self.favorite.append(id)

    def remove_favorite(self, id):
        self.favorite.remove(id)
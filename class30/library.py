class library:
    def __init__(self):
        self.booklst=[]
    def add(self,book):
        self.booklst.append(book)
    def take(self,isbn):
        self.booklst.remove(book for book in self.booklst if book[isbn]==isbn)
    def search_author(self,author):
        print(self.booklst(book for book in self.booklst if book[author]==author))
    def sarch_title(self,titel):
        print(self.booklst(book for book in self.booklst if book[titel]==titel))


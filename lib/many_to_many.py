class Book:
    '''templates a book'''
    all = []
    def __init__(self, title):
        '''initialize attributes'''
        self.title = title
        Book.all.append(self)
    @property
    def title(self):
        '''get title'''
        return self._title
    @title.setter
    def title(self, book_title):
        '''set title with validation'''
        if not isinstance(book_title, str):
            raise Exception("title MUST be a STRING")
        else:
            self._title = book_title
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    '''templates an author'''
    all = []
    def __init__(self, name):
        '''initialize attributes'''
        self.name = name
        Author.all.append(self)
    @property
    def name(self):
        '''get name'''
        return self._name
    @name.setter
    def name(self, author_name):
        '''set name on validation'''
        if not isinstance(author_name, str):
            raise Exception("Author name MUST be a string")
        else:
            self._name = author_name
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        author_royalties_list = [contract.royalties for contract in self.contracts()]
        return sum(author_royalties_list)

class Contract:
    '''blueprints a contract'''
    all = []
    def __init__(self, author, book, date, royalties):
        '''initialize attributes'''
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    @property
    def author(self):
        '''get author'''
        return self._author
    @author.setter
    def author(self, the_author):
        '''set author on validation'''
        if not isinstance(the_author, Author):
            raise Exception("the author must be an instance of Author")
        else:
            self._author = the_author
    @property
    def book(self):
        '''get book'''
        return self._book
    @book.setter
    def book(self, the_book):
        '''set validated book'''
        if not isinstance(the_book, Book):
            raise Exception("the book must be an object of Book")
        else:
            self._book = the_book
    @property
    def date(self):
        '''get date'''
        return self._date
    @date.setter
    def date(self, the_date):
        '''set validated date'''
        if not isinstance(the_date, str):
            raise Exception("The date must be a string")
        else:
            self._date = the_date
    @property
    def royalties(self):
        '''get royalties'''
        return self._royalties
    @royalties.setter
    def royalties(self, the_royalties):
        '''set validated royalties'''
        if not isinstance(the_royalties, int):
            raise Exception("Royalties must be an integr")
        else:
            self._royalties = the_royalties
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
        

#testss
book = Book("Title")
author = Author("Name")
date = '01/01/2001'
royalties = 40000
contract = Contract(author, book, date, royalties)


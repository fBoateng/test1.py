book_list = []
n = int(input('Please enter the number of books you are entering? '))


def addbook(none):
    for i in range(0, n):
        print('Please enter author and title')
        info = [input('Please enter author'), input('Please enter book title')]
        book_list.append(info)
    print(f'Books entered are {book_list}')

addbook(book_list)
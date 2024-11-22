from interface.interface import Inter

class Book(Inter):
    '''
    Основной класс приложения, инициализируется,
    продолжает работать пока не завершить сеанс введя "q" или "quit"
    '''
    def __init__(self):
        '''
        Функция инициализации класса.
        '''
        super().__init__()

        print('Библиотека книг.')
        self.support() #Вызывает метод подсказки
        self.start() # Метод начала работы и управления

    def support(self):
        '''
        Функция подсказки указывает управление приложения
        '''
        print(
            '''
Управление библиотекой:
Для управления используйте цифры!
            
1 - Показать всю библиотеку
2 - Добавить новую книгу
3 - Удалить книгу
4 - Для поиска книги
5 - Для изменения статуса наличия книги

Что бы покинуть библиотеку введите "q" или "quit"
            
0 - Показать подсказку
            '''
        )

    def start(self):
        '''
        Функция отвечает за работу и вызывает управление приложения
        '''
        key = input('Ввод: ')
        if key:
            self.drive(key)

    def drive(self, key):
        '''
        Функция отвечает за управление приложением,
        принимает параметр key, который является числом с соответствующим действием управления
        '''
        if key in [1, '1']:
            self.show_books()
            self.start()
        elif key in [0, '0']:
            self.support()
            self.start()
        elif key in [2, '2']:
            self.create_json()
            self.start()
        elif key in [3, '3']:
            num = input('Введите id книги на удаление: ')
            self.del_book(num)
            self.start()
        elif key in [4, '4']:
            print('Необходимо выбрать критерий для поиска:')
            title = input(
                '1 - Искать по названию\n'
                '2 - Искать по автору\n'
                '3 - Искать по году\n'
                '- '
            )
            if title in [1, '1']:
                title = 'title'
            elif title in [2, '2']:
                title = 'author'
            elif title in [3, '3']:
                title = 'year'
            else:
                print('Не верное значение')
                self.drive(4)
            input_title = input('Введите что необходимо найти: ')
            self.search_book(title, input_title)
            self.start()
        elif key in [5, '5']:
            id = input('Введите id книги: ')
            new_status = input(
                'Новый статус книги\n'
                '0 - если книга выдана\n'
                '1 - если книга в наличии\n'
                '- '
            )
            self.status_book(id, new_status)
            self.start()
        elif key in ['quit', 'q']:
            print('Приятного чтения :)')


if __name__=='__main__':
    '''
    Основной цикл работы приложения, если запускается текущий файл,
    то приложение инициализируется и работает
    '''
    app = Book()
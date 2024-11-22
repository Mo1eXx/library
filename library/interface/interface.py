import json

from schema.classes import Book


class Inter(Book):
    '''Класс содзания и записи данных в json.'''
    def __init__(self):
        '''Функция инициализации класса.'''

    def write_file(self, data):
        '''Функция записи данных в json.'''
        with open('db.json', 'w') as file:
            file.write(
                json.dumps(data, indent=2, ensure_ascii=False)
            )

    def create_json(self):
        '''
        Функция запрашивает данные пользователя и пытается их записать,
        если запись не получается,
        функция создаст новый файл json и внесет данные туда.
        '''
        status = 'В наличии'
        if self.status == False:
            status = 'Выдана'
        json_data = [{
            'id': self.id,
            'title': input('title: '),
            'author': input('author: '),
            'year': input('year: '),
            'status': status,
        }]
        if json_data[0]['year'] is not int():
            print('год должен быть цифрами')
        else:
            try:
                data = json.load(open('db.json')) # Заполняет данные в память, для последующего обновления json
                json_data[0]['id'] = data[-1]['id'] + 1 # Быстрый способ добавить id новой записи
                data.append(json_data[0])
                self.write_file(data) #Эта функция инициализирована выше, что бы избежать дублирования
                print('Книга создана')
            except:
                self.write_file(json_data)
                print('Создана новая библиотека')

    def del_book(self, num):
        '''Функция удаления книги.'''
        try: # Обработка ошибки ввода
            data = json.load(open('db.json'))
            data.pop(int(num)-1)
            len_list = len(data)
            for id_list in range(len_list): # Список переберает id и устанавливает новые
                data[id_list]['id'] = id_list + 1
            self.write_file(data)
            print('Книга удалена')
        except Exception as err:
            print(err,'\nВведите другое значение!')

    def search_book(self, title, input_title):
        '''Функция поиска книг.'''
        try:
            data = json.load(open('db.json'))
            for item in range(len(data)):
                if data[item][title] == input_title:
                    print(list(data[item].values()))
                    break
                else:
                    print('Нет соответствий')
                    break
        except:
            print('Не получилось найти, попробуйте ещё раз!')

    def status_book(self, id, new_status):
        try:
            data = json.load(open('db.json'))
            len_data = len(data)
            if int(id) in range(0, len_data) and new_status in [0, 1, '0', '1']:
                if new_status in [0, '0']:
                    status_book = 'Выдана'
                elif new_status in [1, '1']:
                    status_book = 'В наличии'
                else:
                    print('Не верное значение!')
                data = json.load(open('db.json'))
                for item in range(len(data)):
                    if data[item] == data[int(id) - 1]:
                        data[item]['status'] = status_book
                self.write_file(data)
                print(list(data[int(id) - 1].values()))
            else:
                print('Значение не входит в предел!')
        except:
            print('Не удалось изменить статус, вероятно что то не так!')

    def show_books(self):
        try:
            data = json.load(open('db.json'))
            for id in range(len(data)):
                print(list(data[id].values()))
        except:
            print(
                '''
Здесь пока ничего нет,
это легко исправить.
                
Нажмите "2" и создайте первую книгу!
Удачи!
                '''
            )

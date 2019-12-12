import os
import sqlite3


def cursore_maker(method):
    """Декоратор, создающий курсор, для работы с бд"""

    def wrapper(self, *args, **kwargs):
        with sqlite3.connect(self.name) as base:
            cur = base.cursor()
            return_value = method(self, cur, *args, **kwargs)
            base.commit()
        return return_value

    return wrapper


class SQLWorker:
    """Это API  для работы с SQLite таблицами, заточенный под основную программу"""

    def __init__(self, name='indexed_files.db'):
        self.name = name

    @cursore_maker
    def make_table(self, cur):
        """Метод, создающий таблицу (если она не существует)"""
        # формат бд описан здесь
        cur.execute("""CREATE TABLE IF NOT EXISTS dump(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                name text NOT NULL,
                path text NOT NULL,
                create_date text NOT NULL,
                last_edit_date NOT NULL,
                weight INTEGER NOT NULL
                );""")

    def fill_the_table(self, data):
        try:
            os.remove(self.name)
        except FileNotFoundError:
            pass
        self.make_table()
        self.add_to_the_table(data)

    @cursore_maker
    def add_to_the_table(self, cur, data):
        """Метод позволяет заполнить таблицу данными, на вход принимает список кортежей"""
        cur.executemany("""INSERT INTO dump(name, path, create_date, last_edit_date, weight) VALUES (?,?,?,?,?)""",
                        data)

    @cursore_maker
    def search_by_sql_request(self, cur, request):
        """Метод необходим для самостоятельных пользователей, которые сами пишут SQL запрос"""
        # можешь использовать его, для расширения функционала или тестов
        return cur.execute(request).fetchall()

    def replace_data(self, data):
        """Замена данных таблицы на новые"""
        os.remove(self.name)
        self.make_table()
        self.fill_the_table(data)

    @cursore_maker
    def get_all_values(self, cur):
        """Возвращает все значения"""
        data = cur.execute("select * from dump").fetchall()
        return data

    @cursore_maker
    def except_sort_and_search(self, cur, request, search_in='name', order_by='name', direction='DESC'):
        """Метод, возвращающий все элементы таблицы содержащие в себе запрос, отсортированные
         по заданному критерию, но исключая запрос"""
        # direction можно передать "ASC", тогда будет от меньшего к большему
        return cur.execute(f"""select * from dump where not({search_in} like '%{request}%')
            ORDER BY {order_by} {direction}""").fetchall()

    @cursore_maker
    def sort_and_search(self, cur, request, search_in='name', order_by='name', direction='DESC'):
        """Метод, возвращающий все элементы таблицы содержащие в себе запрос, отсортированные по заданному критерию"""
        # direction можно передать "ASC", тогда будет от меньшего к большему
        return cur.execute(f"""select * from dump where {search_in} like '%{request}%'
            ORDER BY {order_by} {direction}""").fetchall()


if __name__ == '__main__':
    from Searcher import FileWorker

    base = SQLWorker()  # скобочки обязательно, там можно передавать имя файла с бд
    file = FileWorker('./test')
    base.make_table()
    base.fill_the_table(file.list_of_files)

    print(base.search_except_parameter('flag'))  # старый код, до рефакторинга, сейчас уже не работает

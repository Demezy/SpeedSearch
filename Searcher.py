import os, time

# os.stat('1111').st_ctime, os.path.getctime('1111')

class FileWorker:
    """Этот модуль необходим для работы с файлами и директориями.
    Вывод форматирован под основную программу."""

    def __init__(self, path):
        self.ROOT_DIR = os.path.abspath(path)  # дабы при пререносе файла программы, код не терял работоспособность
        os.chdir(self.ROOT_DIR)  # переход в директорию, в которой происходит дальнейшая работа
        self.list_of_files = []  # коллекция файлов и путей до них
        self.refresh()  # заполнение коллекции

    def refresh(self):
        """обновление или добавление файлов в список, к тому же понятное название метода"""
        self.recursive_search(self.ROOT_DIR)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    def test_connect(self):
        """этот метод необходим для проверки работоспособности класса,
         практического применения не несет."""
        print(self.ROOT_DIR, '\n', self.list_of_files)
        return True

    def recursive_search(self, path):
        """Метод рекурсивно определяющий названия файлов и пути к ним и некоторые другие данные
        Ничего не возвращает, запись идет в self.list_of_files"""
        # тут есть некоторые костыли, но это особенности работы python,
        # а не моя инициатива, я потратил 9 часов, чтобы понять эту особенность, сжальтесь.
        os.chdir(path)
        current_dirs, current_files = self.search(path)
        for i in current_files:
            self.list_of_files.append((i, os.path.abspath(path), *self.get_info_about_file(i)))
        for i in current_dirs:
            try:
                os.chdir(os.path.join(path, i))
                # os.chdir(os.path.abspath(i))
                self.recursive_search(os.path.abspath('.'))
            except FileNotFoundError:
                print('ERROR')
                # print(os.path.join(path, i))
                print(os.path.abspath('.'))
            except PermissionError:
                pass

    def search(self, path):
        """Вспомогательный метод, необходимый для рекурсивного.
        Можно использовать и отдельно.
        Возвращает данные ввиде: (dirs, files).
        Выделен отдельно от recursive_search для создания API"""
        return list(filter(lambda x: os.path.isdir(x), os.listdir(path=path))), list(
            filter(lambda x: os.path.isfile(x), os.listdir(path=path)))

    def get_info_about_file(self, name):
        """Этот метод предназначен для получения информации о файле.
        возвращает данные ввиде кортежа: (дата создания, дата изменения, вес в байтах)
        """
        # вынесено отдельно, для последующей возможности изменения.

        file = os.stat(name)
        return time.strftime('%x-%X', time.gmtime(file.st_ctime)), time.strftime('%x-%X', time.gmtime(
            file.st_mtime)), file.st_size


if __name__ == '__main__':
    # print(time.strftime('%x-%X', time.gmtime(12553595355)))
    pass

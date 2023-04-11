from processor.dataprocessor_service import DataProcessorService

import pandas
"""
    Main-модуль, т.е. модуль запуска приложений ("точка входа" приложения)
"""


if __name__ == '__main__':
    # Без указания полного пути, программа будет читать файл из своей корневой папки
    DataProcessorService("UNdata_Export_20230404_121757663.csv").run_service()

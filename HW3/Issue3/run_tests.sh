#!/bin/bash

# Останавливаем скрипт, если есть ошибка при запуске тестов
set -e

# Очистка файла результатов или создание нового, если он не существует
> 'result.txt'

# Запускаем линтер
echo "Running Ruff for PEP8 compliance check..."
ruff check test_transform.py | tee -a result.txt

# Если линтер не ругается, переходим к UnitTest
echo 'Running UnitTest'
python -m unittest test_transform.py 2>&1 | tee -a result.txt

# Проверка завершена
echo "All tests are done!" | tee -a result.txt
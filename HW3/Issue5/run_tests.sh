#!/bin/bash

# Останавливаем скрипт, если есть ошибка при запуске тестов
set -e

# Очистка файла результатов или создание нового, если он не существует
> 'result.txt'

# Запускаем линтер
echo "Running Ruff for PEP8 compliance check..."
ruff check year.py | tee -a result.txt

# Если линтер не ругается, переходим к PyTest
echo 'Running PyTest'
python -m year 2>&1 | tee -a result.txt

coverage run -m unittest year.py && coverage html
echo "All tests are done!" | tee -a result.txt
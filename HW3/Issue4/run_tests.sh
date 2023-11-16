#!/bin/bash

# Останавливаем скрипт, если есть ошибка при запуске тестов
set -e

# Очистка файла результатов или создание нового, если он не существует
> 'result.txt'

# Запускаем линтер
echo "Running Ruff for PEP8 compliance check..."
ruff check test_transform_pytest.py | tee -a result.txt

# Если линтер не ругается, переходим к PyTest
echo 'Running PyTest'
pytest -v test_transform_pytest.py 2>&1 | tee -a result.txt

# Проверка завершена
echo "All tests are done!" | tee -a result.txt
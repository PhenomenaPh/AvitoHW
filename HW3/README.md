# Инструкция по Запуску Тестов

Данная инструкция поможет вам запустить тесты для каждого задания.

## Предварительные Требования

Перед началом работы убедитесь, что на вашем компьютере установлены Python версии 3.10 или выше и инструмент `ruff`. Если эти компоненты отсутствуют, установите их, следуя указаниям в файле `pyproject.toml`.

## Общие Инструкции для Unix-подобных Систем

Для Unix-подобных систем (включая Linux и MacOS) выполните следующие шаги:

1. Склонируйте репозиторий или загрузите необходимые файлы на ваш компьютер.
2. Откройте терминал и перейдите в директорию с файлами задачи.
3. Сделайте скрипт `run_tests.sh` исполняемым командой:
   ```bash
   chmod +x run_tests.sh
   ```
4. Запустите скрипт:
   ```bash
   ./run_tests.sh
   ```

## Общие Инструкции для Windows

Для Windows выполните следующие шаги:

1. Перейдите в директорию с файлами через проводник или с помощью командной строки.
2. Откройте PowerShell и запустите соответствующие команды для вашей задачи.

## Задача 1

### Инструкции для Windows

Запустите следующие команды в PowerShell:
```bash
ruff check morse.py | Out-File result.txt
python -m doctest -v morse.py | Out-File result.txt -Append
```

## Задача 2

### Инструкции для Windows

Запустите следующие команды в PowerShell:
```bash
ruff check morse.py | Out-File result.txt
pytest morse.py | Out-File result.txt -Append
```

## Задача 3

### Инструкции для Windows

Запустите следующие команды в PowerShell:
```bash
ruff check test_transform.py | Out-File result.txt
python -m unittest test_transform.py | Out-File result.txt -Append
```

## Задача 4

### Инструкции для Windows

Запустите следующие команды в PowerShell:
```bash
ruff check test_transform_pytest.py | Out-File result.txt
pytest -v test_transform_pytest.py | Out-File result.txt -Append
```

## Задача 5

### Инструкции для Windows

Запустите следующие команды в PowerShell:
```bash
ruff check year.py | Out-File result.txt
coverage run -m unittest discover & coverage html | Out-File result.txt -Append
```

# Инструкции для запуска тестов

Эти инструкция поможет Вам запустить doctest и проверку flake8 для файла `morse.py`.

## Предварительные требования

Убедитесь, что у вас установлены Python 3.10 или выше и ruff.

## Инструкции (Unix systems)

1. Склонируйте репозиторий или загрузите файлы `morse.py` и `run_tests.sh` на ваш компьютер.
2. Откройте терминал и перейдите в директорию с файлами (Issue1).
3. Сделайте скрипт `run_tests.sh` исполняемым:

```bash
chmod +x run_tests.sh
```

4. Запустите скрипт:
```bash
./run_tests.sh
```
## Инструкция Windows

1. Перейдите в директорию с файлами
2. Запустите код в терминале powershell
```bash
ruff check morse.py | Out-File result.txt
python -m doctest -v morse.py | Out-File result.txt -Append

```
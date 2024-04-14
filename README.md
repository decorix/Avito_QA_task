# Avito_QA_task. Инструкция по эксплуатации

## Архитектура проекта
### Task 1
1. TASK_1.md - информация о решении task №1
2. Task_1.pdf - решение task №1
### Task 2
1. test_first.py - код с автоматизированными тест-кейсами.
2. Директория /output/ - папка с результат-изображениями тест-кейсов.
3. Директория /venv/ - настроенное виртуальное окружение.
4. BUGS.md - файл, содержащий баг-репорты по тест-кейсам.
5. TESTCASES.md - описание тест-кейсов.


## Инструкция по эксплуатации
1. Инициализировать папку с проектом (cmd: git init).
2. Склонировать репозиторий (cmd: git clone https://github.com/decorix/Avito_QA_task.git).
3. Установить требуемые модули для работы с проектом через терминал IDE.
</br>3.1  Pytest (cmd: pip install pytest).
</br>3.2  Playwright (cmd: pip install Playwright).
</br>3.3  pytest-playwright (cmd: pip install pytest-playwright).
</br>3.4  playwright (cmd: playwright install).
4. Запустить проект через терминал (cmd: pytest).
</br> Удалять изображения из директории output не требуется. После выполнения теста, соответствующее ему изображение автоматически обновится.




# Конвертер учебного конфигурационного языка
Данный инструмент командной строки предназначен для преобразования текста из формата JSON в учебный конфигурационный язык. Инструмент выявляет синтаксические ошибки и выводит соответствующие сообщения. Входной текст в формате JSON принимается из стандартного ввода, а выходной текст в учебном конфигурационном языке сохраняется в файл, путь к которому задается ключом командной строки.

## Описание
- ### Синтаксис учебного конфигурационного языка
Массивы: #( значение, значение, значение, ... )
- ### Словари:
{ имя => значение, имя => значение, имя => значение, ... }
- ### Имена: [a-zA-Z][_a-zA-Z0-9]*
- ### Значения:
Числа
Строки
Массивы
Словари
- ### Строки: 'Это строка'
- ### Объявление константы на этапе трансляции: имя: значение
- ### Вычисление константы на этапе трансляции: [имя]
## Примеры описания конфигураций

{
    "_constants": {
        "DEFAULT_PORT": 8080,
        "MAX_CONNECTIONS": 1000
    },
    "server": {
        "host": "localhost",
        "port": "[DEFAULT_PORT]",
        "max_connections": "[MAX_CONNECTIONS]",
        "paths": {
            "static": "/static",
            "templates": "/templates"
        },
        "allowed_origins": ["http://localhost:3000", "https://example.com"]
    }
}

## Требования
Для работы конвертера необходимо наличие следующих компонентов:

- Python 3.6 или новее
- pytest (для запуска тестов)
## Установка
- ### Клонируйте репозиторий с проектом:
git clone https://github.com/v-silence/Config_translator.git
- ### Перейдите в директорию проекта:
cd Config_translator
- ### Установите необходимые зависимости
## Использование
python Config-Translator.py -i 'config2.json'  -o 'output.conf'
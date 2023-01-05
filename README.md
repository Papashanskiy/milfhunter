Для запуска понадобится python и pip

Cперва создай виртуальное окружение
python -m venv venv

Затем установи зависимости
pip install -r requirements.txt

Уже после этого можно запускать приложение
python main.py --login=логин --password=пароль

Что бы открыть полный список опций, необходимо вызвать команду help
python main.py --help

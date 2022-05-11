python manage.py shell
timeout 3
exec(open('nombres.py', encoding="utf-8").read())
exit()
python manage.py runserver
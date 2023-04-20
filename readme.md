* ## pip install
            django
            celery
            django-ckeditor
            https://github.com/froala/django-froala-editor/archive/master.zip
            django-filter
            django-allauth
            django_ckeditor_5 -- не используется, но всё равно требует установить. Так и не нашёл где ещё остались следы.
            redis
            django-apscheduler

* ## superuser
      user: Barsik
      password: qwe
      email: qwe@qwe.qwe

# Рассылка сообщений идёт через celery 
* ## Запуск celery:
        Windows10 -- celery -A game_forum worker -l INFO --pool=solo
        Ubuntu 22.04.2 LTS -- celery -A game_forum worker -l INFO
* ## Если celery не заработает:
      forum/tasks.py строка 6 заменяем на mail_sender(mail)

* ## Очистка базы от не верифицированных пользователей и связанных с ними объектами:
      python3 manage.py runapscheduler

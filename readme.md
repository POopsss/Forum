
---

---

## Здравствуйте, Олег!

Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки.

Заранее спасибо!

---

---
 
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

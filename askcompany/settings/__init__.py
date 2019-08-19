# python manage.py runserver를 하면
# manage.py 보면 askcompany.seetings를 참조하는데 그게 지금은
# 이 __init__.py임
# 근데 여기 아무것도 없으니까 manage.py에서 askcompany.settings.dev로 해주던가~ 하면됨
# wsgi.py에서도 마찬가지
import pymysql

pymysql.install_as_MySQLdb()
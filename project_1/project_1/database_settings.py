DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'login',
        'USER' : 'root',
        'PASSWORD' : 'diligent0924!',
        'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

SECRET_KEY = 'django-insecure-l@7jcl9nn39y@d^h)v0xnac5^ud5(fg7ve)v9%%byjxosfi^er'
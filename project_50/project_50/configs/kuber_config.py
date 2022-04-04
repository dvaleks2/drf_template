SECRET_KEY = "__SECRET_KEY__"
API_VERSION = "__API_VERSION__"
DEBUG = "__DEBUG__"
ALLOWED_HOSTS = "__ALLOWED_HOSTS__"
SSL = "__SSL__"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '__DB_NAME__',
        'USER': '__DB_USER__',
        'PASSWORD': '__DB_PASSWORD__',
        'HOST': '__DB_HOST__',
        'PORT': '__DB_PORT__'
    }
}
REDIS_HOST = "__REDIS_HOST__"
REDIS_PORT = "__REDIS_PORT__"

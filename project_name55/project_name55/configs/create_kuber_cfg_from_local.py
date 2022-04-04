import project_name5.project_name5.configs.local_config

items = [i for i in vars(local_config).items()
         if i[0].isupper() and not i[0].startswith('__')]

with open('kuber_config.py', 'w') as file:
    for item in items:
        if item[0] == 'DATABASES':
            file.write(
"""
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
"""
            )
        else:
            file.write(f'{item[0]} = "__{item[0]}__"\n')

print('done! Write kuber_config.py from local_config.py')

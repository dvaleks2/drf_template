import project_name5.project_name5.configs.local_config

items = [i for i in vars(local_config).items()
         if i[0].isupper() and not i[0].startswith('__')]

with open('example_config.py', 'w') as file:
    for item in items:
        if isinstance(item[1], bool) \
                or item[0] in ['DATABASES', 'API_VERSION',
                               'ALLOWED_HOSTS'] \
                or item[0].endswith('_PORT'):
            value = item[1]
            if isinstance(value, str):
                value = f'"{value}"'
            file.write(f'{item[0]} = {value}\n')
        else:
            file.write(f'{item[0]} = "__{item[0]}__"\n')

print('done! Write example_config.py from local_config.py')

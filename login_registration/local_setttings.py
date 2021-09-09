DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'UserRegistrationLogin',

        'USER': 'postgres',

        'PASSWORD': 'postgres',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}



# import psycopg2
# db_settings = DATABASES['default']
# db_name = db_settings['NAME']
# db_user = db_settings['USER']
# db_pwd = db_settings['PASSWORD']
# db_host = db_settings['HOST']
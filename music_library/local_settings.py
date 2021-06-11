

SECRET_KEY = 'j3igfje_gvqtp^hh$(*2ljrg#0ll&m_v($-6^c&&zfzg4hg9k!'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_db',
        'USER': 'root',
        'PASSWORD': 'P@$$w0rd1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

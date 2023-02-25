WSGI_APPLICATION = 'eval.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'evaluationsicoge',
        'USER': 'webadmin',
        'PASSWORD': 'ODFvns88312',
        'HOST': 'node84021-sicoge-eval-db.jcloud-ver-jpe.ik-server.com',
        'PORT': '5432',
    }
}

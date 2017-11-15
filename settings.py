# Django settings for web project.
from django.conf import global_settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Roberto Estrada', 'restrada@paridin.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'paridin_pygenetics',                      # Or path to database file if using sqlite3.
        'USER': 'paridin_paridin',                      # Not used with sqlite3.
        'PASSWORD': 'pygenetics1234',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Mexico_City'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-MX'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/paridin/public_html/pyGenetics/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://pygenetics.paridin.com/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&w6ut^sn#m^4re*56gksrt-&6u%p))(vmdo8)2wl599c00du$-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)

ROOT_URLCONF = 'pyGenetics.urls'

TEMPLATE_DIRS = (
    '/home/paridin/public_html/pyGenetics/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    'pyGenetics.execute',
    'pyGenetics.comment',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    #'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)


TEMPLATE_DEBUG = True

# cuando esta en modo debug se puede utilizar la debugbar
ACTIVAR_DEBUG_BAR=False # no siempre en debug se quiere la toolbar
if DEBUG and ACTIVAR_DEBUG_BAR:
    MIDDLEWARE_CLASSES+=('pyGenetics.debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS+=('pyGenetics.debug_toolbar',)
    INTERNAL_IPS = ('174.122.135.242',)
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    def custom_show_toolbar(request):
        return True # Always show toolbar, for example purposes only.

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
        #'EXTRA_SIGNALS': ['myproject.signals.MySignal'], tengo una bajaga idea de la utilidad de esto
        'HIDE_DJANGO_SQL': False,
    }


FILE_UPLOAD_PERMISSIONS = 0o644

FILE_UPLOAD_HANDLERS = ['uploadprogresscachedhandler.UploadProgressCachedHandler'] \
+ global_settings.FILE_UPLOAD_HANDLERS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '174.122.135.242:11211',
    }
}

#LOGGING DEBUG
LOG_FILENAME = '/home/paridin/tmp/log/'


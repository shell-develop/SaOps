#_*_coding:utf-8_*_
"""
Django settings for cmdb project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,djcelery,platform

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if platform.system() == "Windows":
    KEY_DIR = "%s\static\ops\key\\" % BASE_DIR
    BASH_DIR = "%s\static\ops\shell\\" % BASE_DIR
else:
    KEY_DIR = "%s/static/ops/key/" % BASE_DIR                           # 密钥配置
    BASH_DIR = "%s/static/ops/shell/" % BASE_DIR                        # 脚本管理目录
    CONF_DIR = "%s/static/ops/config/" % BASE_DIR                       # 配置文件目录
    SQL_DIR = "%s/static/ops/sql_update/" % BASE_DIR                    # 数据库更新文件上传目录
    GAMELIST_DIR = "%s/static/ops/server_list/" % BASE_DIR              # 区服列表目录
    EXCEL_DIR = "%s/static/ops/excels" % BASE_DIR                       # excel 生成目录
    LOG_DIR = "/data/logs"                                            # 日志目录

    # 以下配置旧在旧项目上有效，新项目已经有全局配置
    INC_CONF_DIR = "%s/static/ops/inc/config/" % BASE_DIR
    INC_SQL_DIR = "%s/static/ops/inc/sql_update/" % BASE_DIR
    INC_GAMELIST_DIR = "%s/static/ops/inc/server_list/" % BASE_DIR
    INC_KEY="%s/inc.key" % KEY_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$#_fc+g%f)o4*(h85jx2qtu&faf(sffx$7-g4z)mu0lls*ql@1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 线上环境修改为False
#DEBUG = False

# 不设置默认为空
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrapform',
    'pagination',
    'hosts',
    'manager',
    'inc',
    'multitask',
    'scripting',
    'rest_framework',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'cmdb.custom_middleware.TestMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'cmdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hosts.context_processors.custom_proc',
            ],
        },
    },
]

WSGI_APPLICATION = 'cmdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cmdb_imdst_com',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':3306,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

AUTH_USER_MODEL = 'manager.UserProfile'
TOKEN_TIMEOUT = 120

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

#分页显示在当前页左右两边的页数
PAGINATION_DEFAULT_WINDOW=3
#每页显示数量
PAGINATION_DEFAULT_PAGINATION=25
#最后一页显示的最小页数，默认为0
PAGINATION_DEFAULT_ORPHANS=0
#当页数不存在时，是否显示404页面
PAGINATION_INVALID_PAGE_RAISES_404=True

CELERY_SEND_EVENTS = True
CELERND_TASK_ERROR_EMAILS = True
BACKEND_URL = 'redis://127.0.0.1:6379/0'
BROKER_URL = 'redis://127.0.0.1:6379/1'
#这是使用了django-celery默认的数据库调度模型,任务执行周期都被存在你指定的orm数据库中
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
#celery 执行任务超时时间
CELERY_TASK_RESULT_EXPIRES = 14400 
#celery worker的并发数 也是命令行-c指定的数目,事实上实践发现并不是worker也多越好,保证任务不堆积,生产环境设置100
CELERYD_CONCURRENCY = 2
#每个worker 执行了多少任务就会死掉
CELERYD_MAX_TASKS_PER_CHILD = 300
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
#定义任务所在模块
CELERY_IMPORTS = ('manager.tasks')
#计划任务时区
CELERY_TIMEZONE = 'Asia/Shanghai'

#session的超时时间设置
SESSION_COOKIE_AGE=60*60
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_SAVE_EVERY_REQUEST=True

#邮件配置
EMAIL_HOST = 'smtp.sina.net'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxxx@imdst.com'
EMAIL_HOST_PASSWORD = 'xxxxxx'
EMAIL_SUBJECT_PREFIX = u'[邮件报警]'
EMAIL_USE_TLS = False
ADMIN_EMAIL = 'leoiceo@gmail.com'

# 文件分发，本地原始目录,保留尾斜杠
FILE_TRANS_DIR="/data/file_dir/"
# 脚本分发，本地原始目录,保留尾斜杠
SCRIPT_MULIT_DIR = "/data/script_dir/"

#OPS域名
OPS_DOMAIN = "myops.imdst.com"

#监控域名
MONITOR_DOMAIN = "jk.imdst.com"

#定义日志
# 导入模块
import logging
import django.utils.log
import logging.handlers

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '%s/django.all.log' % LOG_DIR,          # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,                        # 文件大小
            'backupCount': 5,                                   # 备份份数
            'formatter': 'standard',                            # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '%s/django.error.log'%LOG_DIR ,
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '%s/django.request.log' %LOG_DIR,
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '%s/django.script.log' %LOG_DIR,
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'hosts': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
        'slg': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
'''
调用方法
import logging
logger = logging.getLogger("hosts")
logger.error('test')
'''

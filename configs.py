import pymysql
pymysql.install_as_MySQLdb()
DOMAINS = ["127.0.0.1", "acr.wzwzx.cn"]
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'wzwzx',
            'USER': '7vtw1hi02bxtjyuyvmjb',
            'PASSWORD': 'pscale_pw_343gf40E6VYQI3hRTchkYxxHIDDZ4XFeXqW1DRwjAfz',
            'HOST': 'us-east.connect.psdb.cloud',
            'PORT': '3306',
            'OPTIONS': {
                {'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}}
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
            }
    }
}

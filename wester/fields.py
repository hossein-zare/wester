from django.db import models

class UnsignedAutoField(models.AutoField):
    def db_type(self, connection):
        return 'bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT'

    def rel_db_type(self, connection):
        return 'bigint(20) UNSIGNED NOT NULL'

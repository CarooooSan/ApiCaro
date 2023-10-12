from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=100, db_column='nombre_Usuario')
    correoUsuario = models.CharField(max_length=100, db_column='correo_Usuario')
    contraUsuario = models.CharField(max_length=128, db_column='contra_Usuario')
    last_login = models.DateTimeField(null=True, blank=True)

    def set_password(self, raw_password):
        self.contraUsuario = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contraUsuario)

    class Meta:
        db_table = 'UsuarioTabla'

class SupUsuario(models.Model):
    idSupUsuario = models.AutoField(primary_key=True)  # Autoincrementable
    nombreSupUsuario = models.CharField(max_length=100,db_column='nombre_SupUsuario')
    correoSupUsuario = models.CharField(max_length=100,db_column='correo_SupUsuario')
    contraSupUsuario = models.CharField(max_length=100,db_column='contra_SupUsuario')
    class Meta:
        db_table='SuperUsuarioTabla'
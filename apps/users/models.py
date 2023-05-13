from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, email, first_name, last_name, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un email')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        #set_password permitira codificar la contraseña como Django la maneja
        user.set_password(password)
        #Guardamos en la base de datos
        user.save(using =self.db)
        return user
    
    def create_user(self, username,email, first_name, last_name, password = None, **extra_fields):
        return self._create_user(username,email, first_name, last_name, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, first_name, last_name, password = None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, True, True, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(max_length=255, unique= True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='perfil/', max_length=255, null = True, blank=True)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = False)
    last_login = models.DateField()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def natural_key(self):
        return (self.username)
    
    def __str__(self):
        #Retornamos el Nombre y apellido del usuario
        return f'{self.first_name} {self.last_name}'
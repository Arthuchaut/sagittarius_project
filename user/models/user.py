from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    '''The custom User model class based on Django default User model.
    
    Attributes:
        USERNAME_FIELD (str): The username field used for authentication.
        REQUIRED_FIELDS (list[str]): The required nullable fields 
            from default model. Empty in our case, cause the email, 
            username and password are already required.
        email (models.EmailField): The user email used for authentication.
    '''

    email: models.EmailField = models.EmailField(
        _('email address'), unique=True
    )
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        '''The User meta class definition.
        
        Attributes:
            app_label (str): The app_label used by Django.?
            db_table (str): The database table name overwriting.
            verbose_name (str): The model verbose name (for documentation).
            verbose_name_plural (str): Same as above, but in plural...
        '''

        app_label: str = 'user'
        db_table: str = 'user'
        verbose_name: str = _('user')
        verbose_name_plural: str = _('users')
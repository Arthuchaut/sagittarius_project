from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User


class UserTag(models.Model):
    '''The UserTag model class.
    
    Attributes:
        name (models.CharField): The tag name.
        icon (models.TextField): The icon binary content.
    '''

    name: models.CharField = models.CharField(
        _('user tag name'), max_length=150, unique=True
    )
    icon: models.TextField = models.TextField(
        _('user tag icon binary'), blank=True, null=True
    )
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        '''The User meta class definition.
        
        Attributes:
            app_label (str): The app_label used by Django.?
            db_table (str): The database table name overwriting.
            verbose_name (str): The model verbose name (for documentation).
            verbose_name_plural (str): Same as above, but in plural...
        '''

        app_label: str = 'transaction'
        db_table: str = 'user_tag'
        verbose_name: str = _('user_tag')
        verbose_name_plural: str = _('user_tags')
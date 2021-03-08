from django.db import models
from django.utils.translation import gettext_lazy as _


class TransactionType(models.Model):
    '''The TransactionType model class.
    
    Attributes:
        type (models.CharField): The type choice.
    '''

    class Type(models.TextChoices):
        INCOME: str = 'INCOME'
        OUTCOME: str = 'OUTCOME'

    type: models.CharField = models.CharField(
        _('transation type'), max_length=7, choices=Type.choices, unique=True
    )

    class Meta:
        '''The User meta class definition.
        
        Attributes:
            app_label (str): The app_label used by Django.?
            db_table (str): The database table name overwriting.
            verbose_name (str): The model verbose name (for documentation).
            verbose_name_plural (str): Same as above, but in plural...
        '''

        app_label: str = 'transaction'
        db_table: str = 'transaction_type'
        verbose_name: str = _('transaction_type')
        verbose_name_plural: str = _('transaction_types')
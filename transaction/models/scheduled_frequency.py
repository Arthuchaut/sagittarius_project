from django.db import models
from django.utils.translation import gettext_lazy as _


class ScheduledFrequency(models.Model):
    '''The ScheduledFrequency model class.
    
    Attributes:
        frequency (models.CharField): The frequency choice.
    '''

    class Freq(models.TextChoices):
        DAILY: str = 'DAILY'
        WEEKLY: str = 'WEEKLY'
        MONTHLY: str = 'MONTHLY'
        YEARLY: str = 'YEARLY'

    frequency: models.CharField = models.CharField(
        _('frequency'), max_length=7, choices=Freq.choices, unique=True
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
        db_table: str = 'scheduled_frequency'
        verbose_name: str = _('scheduled_frequency')
        verbose_name_plural: str = _('scheduled_frequencies')
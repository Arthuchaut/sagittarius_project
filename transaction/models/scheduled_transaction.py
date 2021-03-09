from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from .transaction_type import TransactionType
from .scheduled_frequency import ScheduledFrequency


class ScheduledTransaction(models.Model):
    '''The ScheduledTransaction model class.
    
    Attributes:
        amount (models.FloatField): The transaction amount.
        transaction_type (models.ForeignKey): The transaction_type related.
        scheduled_frequency (models.ForeignKey): The scheduled_frequency related.
        user (models.ForeignKey): The user related.
    '''

    amount: models.FloatField = models.FloatField(_('amount'))
    transaction_type: models.ForeignKey = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE,
    )
    scheduled_frequency: models.ForeignKey = models.ForeignKey(
        ScheduledFrequency,
        on_delete=models.CASCADE,
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
        db_table: str = 'scheduled_transaction'
        verbose_name: str = _('scheduled_transaction')
        verbose_name_plural: str = _('scheduled_transactions')
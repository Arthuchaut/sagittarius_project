from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from .user_tag import UserTag
from .default_tag import DefaultTag
from .transaction_type import TransactionType


class TransactionManager(models.Manager):

    def create(self, **kwargs: dict[str, Any]) -> object:
        '''Overwrite the QuerySet.create() method.
        Adding XOR foreign key constraints for UserTag and DefaultTag relations.

        Args:
            **kwargs (dict[str, Any]): The transaction fields.
        
        Raises:
            ValueError: If XOR constraint is not valid.

        Returns:
            Transaction: The transaction object created.
        '''

        if kwargs.get('user_tag') and kwargs.get('default_tag'):
            raise ValueError(
                'UserTag and DefaultTag can\'t be declared '
                'in the same transaction.'
            )

        transaction: object = self.model(**kwargs)
        self._for_write = True
        transaction.save(force_insert=True, using=self.db)

        return transaction


class Transaction(models.Model):
    '''The UserTag model class.
    
    Attributes:
        amount (models.FloatField): The transaction amount.
        created_date (models.DateTimeField): The transaction datetime.
        user (models.ForeignKey): The User related to the transaction.
        transaction_type (models.ForeignKey): The TransactionType related 
            to the transaction.
        user_tag (models.ForeignKey): The UserTag related to the transaction.
            Note: UserTag and Default can't exists for the same transaction.
        default_tag (models.ForeignKey): The DefaultTag related 
            to the transaction.
            Note: UserTag and Default can't exists for the same transaction.
    '''

    amount: models.FloatField = models.FloatField(_('transaction amount'))
    created_date: models.DateTimeField = models.DateTimeField(
        _('transaction datetime'), auto_now_add=True
    )
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type: models.ForeignKey = models.ForeignKey(
        TransactionType, on_delete=models.CASCADE
    )
    user_tag: models.ForeignKey = models.ForeignKey(
        UserTag, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    default_tag: models.ForeignKey = models.ForeignKey(
        DefaultTag, on_delete=models.DO_NOTHING, blank=True, null=True
    )

    objects: TransactionManager = TransactionManager()

    class Meta:
        '''The User meta class definition.
        
        Attributes:
            app_label (str): The app_label used by Django.?
            db_table (str): The database table name overwriting.
            verbose_name (str): The model verbose name (for documentation).
            verbose_name_plural (str): Same as above, but in plural...
        '''

        app_label: str = 'transaction'
        db_table: str = 'transaction'
        verbose_name: str = _('transaction')
        verbose_name_plural: str = _('transactions')
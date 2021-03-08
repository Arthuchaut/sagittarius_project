import pytest
from transaction.models import TransactionType


class TestTransactionType:
    '''The TransactionType model test class.
    '''

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize(
        'type', [
            (TransactionType.Type.INCOME, ),
            (TransactionType.Type.OUTCOME, ),
            pytest.param('foo', marks=pytest.mark.xfail),
            pytest.param(None, marks=pytest.mark.xfail),
        ]
    )
    def test_create(self, type: TransactionType.Type) -> None:
        '''Test the transaction_type creation.
        '''

        trans_type: TransactionType = TransactionType.objects.create(type=type)
        assert trans_type
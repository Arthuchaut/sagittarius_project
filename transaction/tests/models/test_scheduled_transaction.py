import pytest
from user.models import User
from transaction.models import ScheduledTransaction, ScheduledFrequency, TransactionType


class TestScheduledTransaction:
    '''The ScheduledTransaction model test class.
    '''

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize(
        'amount, has_trans_type, has_frequency', [
            (42.0, True, True),
            pytest.param(42.0, True, False, marks=pytest.mark.xfail),
            pytest.param(None, True, True, marks=pytest.mark.xfail),
            pytest.param(42.0, False, True, marks=pytest.mark.xfail),
            pytest.param('foo', True, True, marks=pytest.mark.xfail),
        ]
    )
    def test_create(
        self, lambda_user: User, amount: float, has_trans_type: bool,
        has_frequency: bool
    ) -> None:
        '''Test the scheduled_transaction creation.
        '''

        trans_type: TransactionType = TransactionType.objects.create(
            type=TransactionType.Type.INCOME
        ) if has_trans_type else None
        frequency: ScheduledFrequency = ScheduledFrequency.objects.create(
            frequency=ScheduledFrequency.Freq.DAILY
        ) if has_frequency else None

        scheduled_trans: ScheduledTransaction = ScheduledTransaction.objects.create(
            amount=amount,
            transaction_type=trans_type,
            scheduled_frequency=frequency,
            user=lambda_user
        )

        assert scheduled_trans
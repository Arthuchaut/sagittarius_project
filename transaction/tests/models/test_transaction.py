import pytest
from user.models import User
from transaction.models import (
    Transaction, TransactionType, UserTag, DefaultTag
)


class TestTransaction:
    '''The Transaction model test class.
    '''

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize(
        'amount, has_trans_type, has_user_tag, has_default_tag',
        [
            (42.0, True, True, False),
            (42.0, True, False, True),
            pytest.param(42.0, True, True, True, marks=pytest.mark.xfail),
            pytest.param(42.0, False, False, True, marks=pytest.mark.xfail),
            pytest.param(None, True, False, True, marks=pytest.mark.xfail),
        ],
    )
    def test_create(
        self,
        lambda_user: User,
        amount: float,
        has_trans_type: bool,
        has_user_tag: bool,
        has_default_tag: bool,
    ) -> None:
        '''Test the transaction creation.
        '''

        transaction_type: TransactionType = TransactionType.objects.create(
            type=TransactionType.Type.INCOME
        ) if has_trans_type else None
        user_tag: UserTag = UserTag.objects.create(
            name='Fake tag', user=lambda_user
        ) if has_user_tag else None
        default_tag: DefaultTag = DefaultTag.objects.create(
            name='Fake tag'
        ) if has_default_tag else None

        transaction: Transaction = Transaction.objects.create(
            amount=amount,
            transaction_type=transaction_type,
            user_tag=user_tag,
            default_tag=default_tag,
            user=lambda_user,
        )

        assert transaction
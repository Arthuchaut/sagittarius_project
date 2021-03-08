import pytest
from user.models import User
from transaction.models import Transaction, TransactionType, UserTag, DefaultTag


class TestTransaction:
    '''The Transaction model test class.
    '''

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize(
        'amount, trans_type_choice, user_tag_name, default_tag_name',
        [
            (42.0, TransactionType.Type.INCOME, 'lambda user tag', None),
            (42.0, TransactionType.Type.INCOME, None, 'lambda default tag'),
            pytest.param(
                42.0,
                TransactionType.Type.INCOME,
                'lambda user tag',
                'lambda default tag',
                marks=pytest.mark.xfail
            ),
            pytest.param(
                42.0,
                None,
                None,
                'lambda default tag',
                marks=pytest.mark.xfail
            ),
            pytest.param(
                None,
                TransactionType.Type.INCOME,
                None,
                'lambda default tag',
                marks=pytest.mark.xfail
            ),
        ],
    )
    def test_create(
        self,
        lambda_user: User,
        amount: float,
        trans_type_choice: TransactionType.Type,
        user_tag_name: str,
        default_tag_name: str,
    ) -> None:
        '''Test the transaction creation.
        '''

        user_tag: UserTag = None
        default_tag: DefaultTag = None
        transaction_type: TransactionType = None

        if user_tag_name:
            user_tag = UserTag.objects.create(
                name=user_tag_name, user=lambda_user
            )
        if default_tag_name:
            default_tag = DefaultTag.objects.create(name=default_tag_name)
        if trans_type_choice:
            transaction_type = TransactionType.objects.create(
                type=trans_type_choice
            )

        transaction: Transaction = Transaction.objects.create(
            amount=amount,
            transaction_type=transaction_type,
            user_tag=user_tag,
            default_tag=default_tag,
            user=lambda_user,
        )
        assert transaction
import pytest
from user.models import User
from transaction.models import UserTag


class TestUserTag:
    '''The User model test class.
    '''

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize(
        'name, icon', [
            ('foo', None),
            ('bar', 'baz'),
            pytest.param(None, 'baz', marks=pytest.mark.xfail),
        ]
    )
    def test_create(self, lambda_user: User, name: str, icon: str) -> None:
        '''Test the user_tag creation.
        '''

        user_tag: UserTag = UserTag.objects.create(
            name=name, icon=icon, user=lambda_user
        )
        assert user_tag
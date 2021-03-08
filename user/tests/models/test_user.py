import pytest
from user.models import User


class TestUser:
    '''The User model test class.
    '''

    @pytest.mark.django_db(transaction=True)
    def test_create_user(self) -> None:
        '''Test the user creation.
        '''

        user: User = User.objects.create_user(
            username='foo', email='foo@bar.org', password='123456'
        )
        assert user

    @pytest.mark.django_db(transaction=True)
    def test_create_superuser(self) -> None:
        '''Test the superuser creation.
        '''

        user: User = User.objects.create_superuser(
            username='foo', email='foo@bar.org', password='123456'
        )
        assert user
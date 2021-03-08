from django.test import TestCase
from user.models import User


class UserTestCase(TestCase):
    '''The User model test class.
    '''

    def test_create_user(self) -> None:
        '''Test the user creation.
        '''

        user_to_create: User = User.objects.create_user(
            username='foo', email='foo@bar.org', password='123456'
        )
        created_user: User = User.objects.filter(id=user_to_create.id).first()

        assert created_user and created_user == user_to_create

    def test_create_superuser(self) -> None:
        '''Test the superuser creation.
        '''

        user_to_create: User = User.objects.create_superuser(
            username='foo', email='foo@bar.org', password='123456'
        )
        created_user: User = User.objects.filter(id=user_to_create.id).first()

        assert created_user and created_user == user_to_create
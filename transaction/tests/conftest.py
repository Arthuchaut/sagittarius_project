import pytest
from _pytest.monkeypatch import MonkeyPatch
from user.models import User


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def lambda_user() -> User:
    user: User = User.objects.create_user(
        username='foo', email='foo@bar.org', password='123456'
    )
    return user

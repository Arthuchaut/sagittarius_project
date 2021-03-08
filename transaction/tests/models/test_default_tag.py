import pytest
from transaction.models import DefaultTag


class TestDefaultTag:
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
    def test_create(self, name: str, icon: str) -> None:
        '''Test the default_tag creation.
        '''

        default_tag: DefaultTag = DefaultTag.objects.create(
            name=name, icon=icon
        )
        assert default_tag
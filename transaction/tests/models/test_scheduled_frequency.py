import pytest
from transaction.models import ScheduledFrequency


class TestScheduledFrequency:
    '''The ScheduledFrequency model test class.
    '''

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.parametrize(
        'frequency', [
            (ScheduledFrequency.Freq.DAILY, ),
            (ScheduledFrequency.Freq.WEEKLY, ),
            (ScheduledFrequency.Freq.MONTHLY, ),
            (ScheduledFrequency.Freq.YEARLY, ),
            pytest.param('foo', marks=pytest.mark.xfail),
            pytest.param(None, marks=pytest.mark.xfail),
        ]
    )
    def test_create(self, frequency: ScheduledFrequency.Freq) -> None:
        '''Test the scheduled_frequency creation.
        '''

        scheduled_freq: ScheduledFrequency = ScheduledFrequency.objects.create(
            frequency=frequency
        )
        assert scheduled_freq
import django_filters
from .models import Profile


class findUser(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['name', 'department']

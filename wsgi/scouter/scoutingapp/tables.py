import django_tables2 as tables
from .models import Match


class MatchTable(tables.Table):
    class Meta:
        model = Match
        # add class="bordered"
        attrs = {'class': 'striped responsive-table'}  # materialze class

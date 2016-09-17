import django_tables2 as tables
from .models import Match


class MatchTable(tables.Table):

    class Meta:
        model = Match
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        sequence = ('match_number', 'scouted_team', 'scouted_by',
                    'team_missed_match', 'auto_defense_crossed',
                    'auto_low_balls', 'auto_high_balls', 'auto_dropped_ball',
                    'low_bar_crossed', 'defense2_crossed', 'defense3_crossed',
                    'defense4_crossed', 'defense5_crossed') 

import django_tables2 as tables
from .models import Match, AllianceMatch, MyUser


class UserTable(tables.Table):
    team_number= tables.Column(accessor='team.team_number')
    class Meta:
        model = MyUser
        fields = ('email', 'team_number')


class MatchTable(tables.Table):

    class Meta:
        model = Match
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        exclude = ('tournament', 'score', 'id')


class AllianceMatchTable(tables.Table):
    class Meta:
        model = AllianceMatch
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        sequence = ('match_number', 'alliance', 'scouted_by',
                    'robot_1_driver_skill',
                    'robot_2_driver_skill', 'robot_3_driver_skill',
                    'robot_1_breach_ability', 'robot_2_breach_ability',
                    'robot_3_breach_ability',
                   )
        exclude = ('id', 'field_setup')
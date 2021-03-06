import django_tables2 as tables
from .models import Match, AllianceMatch, MyUser, CubePlace, CubeScored, CubeAcquired, CubeWhen, Team


class UserTable(tables.Table):
    team_number = tables.Column(accessor='team.team_number')

    class Meta:
        model = MyUser
        fields = ('email', 'team_number')


class MatchTable(tables.Table):
    export_formats = ['csv']
    class Meta:
        model = Match
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        exclude = ('tournament', 'score', 'id', 'created_at', 'updated_at')
        sequence = ('match_number', 'scouted_team', 'auto_move_yn',
                    'robot_end_game', 'robot_card', 'scouted_by', 'duplicate')


class TeamTable(tables.Table):

    class Meta:
        model = Team
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        sequence = ('team_number', 'team_name', 'currently_in_event')

class ViewMatchTable(tables.Table):
    # ground = tables.Column(accessor='has_ground', verbose_name='Can pick up from ground')

    class Meta:
        model = Match
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        exclude = ('tournament', 'score', 'id', 'created_at', 'updated_at')
        sequence = ('match_number', 'scouted_team', 'auto_move_yn',
                    'robot_end_game', 'robot_card', 'scouted_by', 'duplicate')


class CubeTable(tables.Table):
    bot = tables.Column(accessor='bot', verbose_name='team')
    class Meta:
        model = CubePlace
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        sequence = {'match', 'bot', 'acquired', 'scored', 'when', 'scouted_by'}

class AllianceMatchTable(tables.Table):
    class Meta:
        model = AllianceMatch
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
#         sequence = ('match_number', 'alliance', 'scouted_by',
#                     'robot_1_driver_skill',
#                     'robot_2_driver_skill', 'robot_3_driver_skill',
#                     'robot_1_breach_ability', 'robot_2_breach_ability',
#                     'robot_3_breach_ability',
#                    )
        exclude = ('id', 'field_setup')


class CategoryTable(tables.Table):
    gearpositions = tables.Column()
    gearsources = tables.Column()
    endgames = tables.Column()
    cards = tables.Column()

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
        exclude = ('tournament', 'score', 'id', 'created_at', 'updated_at')
        sequence = ('match_number', 'scouted_team', 'auto_gears_scored', 'auto_move_yn', 'auto_hopper_triggered', 'auto_hopper_load', 'auto_high_goal_accuracy', 'auto_low_goal_accuracy', 'teleop_hoppers_triggered', 'robot_end_game', 'robot_card', 'scouted_by', 'duplicate', 'gears_scored', 'gears_dropped', 'gears_type')

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
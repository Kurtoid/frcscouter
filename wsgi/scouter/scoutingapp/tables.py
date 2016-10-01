import django_tables2 as tables
from .models import Match, FieldSetup, AllianceMatch, MyUser


class FieldTable(tables.Table):
    class Meta:
        model = FieldSetup


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
        sequence = ('match_number', 'scouted_team', 'scouted_by',
                    'team_missed_match', 'auto_defense_crossed',
                    'auto_low_goal', 'auto_high_goal', 'auto_dropped_ball',
                    'low_bar_crossed', 'defense2_crossed', 'defense3_crossed',
                    'defense4_crossed', 'defense5_crossed', 'fed_boulder',
                    'dropped_boulders', 'low_goals_scored', 'high_goals_missed',
                    'high_goals_scored', 'robot_end_game', 'robot_card',
                   )
        exclude = ('tournament', 'score', 'id')


class AllianceMatchTable(tables.Table):
    defense2_type = tables.Column(accessor='field_setup.defense2')
    defense3_type = tables.Column(accessor='field_setup.defense3')
    defense4_type = tables.Column(accessor='field_setup.defense4')
    defense5_type = tables.Column(accessor='field_setup.defense5')
    class Meta:
        model = AllianceMatch
        # add class="bordered"
        attrs = {'class': 'bordered responsive-table'}  # materialze class
        sequence = ('match_number', 'alliance', 'scouted_by',
                    'defense2_type', 'defense3_type', 'defense4_type',
                    'defense5_type', 'robot_1_driver_skill',
                    'robot_2_driver_skill', 'robot_3_driver_skill',
                    'robot_1_breach_ability', 'robot_2_breach_ability',
                    'robot_3_breach_ability',
                   )
        exclude = ('id', 'field_setup')

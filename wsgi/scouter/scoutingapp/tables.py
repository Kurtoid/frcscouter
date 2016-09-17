import django_tables2 as tables
from .models import Match, FieldSetup, AllianceMatch


class FieldTable(tables.Table):
    class Meta:
        model = FieldSetup


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
                    'robot_1_end_game', 'robot_2_end_game', 'robot_3_end_game',
                    'robot_1_breach_ability', 'robot_2_breach_ability',
                    'robot_3_breach_ability', 'robot_1_card', 'robot_2_card',
                    'robot_3_card'
                   )
        exclude = ('id', 'field_setup')

fantasy_scoring = {
    'passing_tds': 6,
    'interceptions': -1,
    'receptions': 1,
    'passing_yards': 0.1,
    'passing_2pt_conversions': 2,
    'rushing_tds': 6,
    'rushing_yards': 0.1,
    'rushing_2pt_conversions': 2,
    'receiving_tds': 6,
    'receiving_yds': 0.1,
    'receiving_2pt_conversions': 2,
    'fg_0_39': 3,
    'fg_40_49': 4,
    'fg_50_59': 5,
    'fg_60': 6,
    'kickoff_return_td': 6,
    'punt_return_td': 6,
    'fumble_for_td': 6,
    'fumble_loss': -2,
    'pick_six': 6,
    'blocked_punt_or_FG_td': 6,
    'fumble_recover': 2,
    'safety': 2,
    'sack': 1,
    '0_pts_allowed': 5,
    '1-6_pts_allowed': 5,
    '7-13_pts_allowed': 5,
    '14-17_pts_allowed': 5,
    '18-27_pts_allowed': 5,
    '28-34_pts_allowed': 5,
    '35-45_pts_allowed': 5,
    '46plus_pts_allowed': 5,
}

unneeded_cols = [
    'player_name',
    'headshot_url',
    'season_type',
    'passing_epa',
    'pacr',
    'dakota',
    'rushing_epa',
    'receiving_epa',
    'racr',
    'air_yards_share',
    'wopr',
    'fantasy_points',
    'fantasy_points_ppr'
]

DEF = ['FS', 'OLB', 'ILB', 'MLB', 'CB', 'DT', 'SS']

SPEC = ['K', 'P', 'KR', 'PR']

RB = ['RB', 'FB']

fantasy_pos_groups = [
    'QB',
    RB,
    'WR',
    'TE',
    'SPEC',        #includes P, K
    DEF
]

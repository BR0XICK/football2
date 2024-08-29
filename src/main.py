import numpy as np
import pandas as pd
from scipy.io import savemat, loadmat

from scoring import fantasy_scoring, unneeded_cols, fantasy_pos_groups

# get positional players qb, wr, rb
def get_position_players(pos: str, data: pd.DataFrame) -> pd.DataFrame:
    return data[data['position'] == pos]

def save_csv_as_mat(csv: str):
    csv_data = pd.read_csv('./data/player_stats_2023.csv')
    data = csv_data.drop(columns=unneeded_cols)
    savemat('./data/fantasy_stats.mat', data)

def load_mat() -> pd.DataFrame:
    try:
        data = loadmat('./data/fantasy_stats.mat')
        return data
    except:
        save_csv_as_mat('./data/player_stats_2023.csv')
        data = loadmat('./data/fantasy_stats.mat')
        return data

def main() -> int:
    stats = load_mat()
    print(stats.keys())
    return 1

if __name__ == "__main__":
    print(main())
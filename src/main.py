import numpy as np
import pandas as pd
from scipy.io import savemat, loadmat

from scoring import fantasy_scoring, unneeded_cols, fantasy_pos_groups

# get positional players qb, wr, rb
def get_position_players(pos: str, data: pd.DataFrame) -> pd.DataFrame:
    return data[data['position'] == pos]

def save_csv_as_mat(csv: str):
    csv_data = pd.read_csv('../player_stats_2023.csv')
    data = csv_data.drop(columns=unneeded_cols)
    savemat('fantasy_stats.mat', data)

def load_mat() -> pd.DataFrame:
    try:
        data = loadmat('./fantasy_stats.mat')
        return data
    except:
        data = loadmat('./fantasy_stats.mat')
        save_csv_as_mat('./player_stats_2023.csv')
        return data

def main() -> int:
    #stats = load_mat()
    #print(stats.keys())
    print("Hello world")
    return 1

if __name__ == "__main__":
    print(main())
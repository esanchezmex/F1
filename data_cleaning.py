import pandas as pd
import os

folder_path = 'season_data'
season_csvs = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Columns to keep
cols = [
    'season', 'round', 'weather_warm', 'weather_cold', 'weather_dry', 'weather_wet', 
    'weather_cloudy', 'driver', 'grid', 'podium', 'driver_points', 'driver_wins', 
    'driver_standings_pos', 'constructor_points', 'constructor_wins', 'constructor_standings_pos', 
    'qualifying_time', 'driver_age', 'circuit_id_adelaide', 'circuit_id_albert_park', 
    'circuit_id_americas', 'circuit_id_bahrain', 'circuit_id_brands_hatch', 'circuit_id_catalunya', 
    'circuit_id_detroit', 'circuit_id_estoril', 'circuit_id_galvez', 'circuit_id_hockenheimring', 
    'circuit_id_hungaroring', 'circuit_id_imola', 'circuit_id_indianapolis', 'circuit_id_interlagos', 
    'circuit_id_istanbul', 'circuit_id_jacarepagua', 'circuit_id_jerez', 'circuit_id_kyalami', 
    'circuit_id_magny_cours', 'circuit_id_marina_bay', 'circuit_id_monaco', 'circuit_id_monza', 
    'circuit_id_nurburgring', 'circuit_id_phoenix', 'circuit_id_red_bull_ring', 'circuit_id_ricard', 
    'circuit_id_rodriguez', 'circuit_id_sepang', 'circuit_id_shanghai', 'circuit_id_silverstone', 
    'circuit_id_sochi', 'circuit_id_spa', 'circuit_id_suzuka', 'circuit_id_valencia', 
    'circuit_id_villeneuve', 'circuit_id_yas_marina', 'circuit_id_yeongam', 'circuit_id_zandvoort', 
    'nationality_American', 'nationality_Australian', 'nationality_Austrian', 'nationality_Belgian', 
    'nationality_Brazilian', 'nationality_British', 'nationality_Canadian', 'nationality_Danish', 
    'nationality_Dutch', 'nationality_Finnish', 'nationality_French', 'nationality_German', 
    'nationality_Italian', 'nationality_Japanese', 'nationality_Mexican', 'nationality_Russian', 
    'nationality_Spanish', 'nationality_Swedish', 'constructor_alfa', 'constructor_arrows', 
    'constructor_bar', 'constructor_benetton', 'constructor_brabham', 'constructor_ferrari', 
    'constructor_footwork', 'constructor_force_india', 'constructor_haas', 'constructor_jaguar', 
    'constructor_jordan', 'constructor_larrousse', 'constructor_ligier', 'constructor_lotus_f1', 
    'constructor_mclaren', 'constructor_mercedes', 'constructor_minardi', 'constructor_prost', 
    'constructor_red_bull', 'constructor_renault', 'constructor_sauber', 'constructor_team_lotus', 
    'constructor_toro_rosso', 'constructor_toyota', 'constructor_tyrrell', 'constructor_williams'
    ]


dfs = [] # Will concat later

try:
    for file in season_csvs:
        df = pd.read_csv(os.path.join(folder_path, file))
        if dfs:
            common_columns = list(set(df.columns) & set(cols))
            df = df[common_columns]
        dfs.append(df)

    all_season_dfs = pd.concat(dfs, axis=0)
    all_season_dfs.sort_values(by='season', inplace=True)
    all_season_dfs.to_csv('ALL_SEASONS.csv', index=False)
except Exception as e:
    print(f"Error: {e}")

print(f"All seasons combined succesfully. Dataframe ready to train models.")
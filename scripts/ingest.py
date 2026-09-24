import pandas as pd
from database.database import SessionLocal
from database.models import Match

csv_file_path = "data/raw/matches.csv"
print(f"Loading and transforming data from {csv_file_path}....")

df = pd.read_csv(csv_file_path)

df = df[['Date','HomeTeam','AwayTeam','FTHG','FTAG']]

df = df.rename(columns={
    'Date': 'match_date',
    'HomeTeam': 'home_team',
    'AwayTeam': 'away_team',
    'FTHG': 'home_goals',
    'FTAG': 'away_goals'
})

df['match_date'] = pd.to_datetime(df['match_date'], dayfirst=True, format='mixed')

print("Connecting to PostgreSQL...")
db = SessionLocal()

try:
    inserted_count = 0
    for index,row in df.iterrows():

        new_match = Match(
            date=row['date'],
            home_team=row['home_team'],
            away_team=row['away_team'],
            home_score=row['home_goals'],
            away_score=row['away_goals'],
        )

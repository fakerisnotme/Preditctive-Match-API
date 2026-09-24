from sqlalchemy import Column, Integer, String, Date, ForeignKey,Float,CheckConstraint
from sqlalchemy.orm import relationship
from database.database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String, unique=True, nullable=False)
    league = Column(String, nullable=False)

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    match_date = Column(Date, nullable=False)

    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)

    full_time_result = Column(String(1), nullable=False)

    home_rolling_xG = Column(Float, nullable=True)
    away_rolling_xG = Column(Float, nullable=True)
    home_rest_days = Column(Integer,nullable = True)
    away_rest_days = Column(Integer, nullable = True)

    home_team = relationship("Team", foreign_keys="Match.home_team_id")
    away_team = relationship("Team", foreign_keys="Match.away_team_id")

    __table_args__ = (

    CheckConstraint('home_team_id != away_team_id', name='check_teams_not_equal')
    )

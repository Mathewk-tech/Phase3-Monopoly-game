from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from engine import engine

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    money = Column(Integer, default=1500)
    position = Column(Integer, default=0)
    in_jail = Column(Boolean, default=False)
    board_id = Column(Integer, ForeignKey("board.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    laps = Column(Integer, default=0)

    
    game = relationship("Game", back_populates="players", foreign_keys=[game_id])
    properties = relationship("Property", back_populates="owner")
    turns = relationship("Turn", back_populates="player")
    transactions = relationship("Transaction", back_populates="player")
    jail = relationship("Jail", back_populates="player")
    
    current_space = relationship("Board")


class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey("players.id"))
    rent = Column(Integer, nullable=False)

    owner = relationship("Player", back_populates="properties")


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    current_turn = Column(Integer, ForeignKey("players.id"))

    current_player = relationship("Player", foreign_keys=[current_turn])
    turns = relationship("Turn", back_populates="game")
    players = relationship("Player", back_populates="game", foreign_keys=[Player.game_id])

class ChanceCard(Base):
    __tablename__ = "chance_cards"
    id = Column(Integer, primary_key=True)
    description = Column(String)


class CommunityChestCard(Base):
    __tablename__ = "community_chest_cards"
    id = Column(Integer, primary_key=True)
    description = Column(String)


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    amount = Column(Integer)

    player = relationship("Player", back_populates="transactions")


class Turn(Base):
    __tablename__ = "turns"
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    player_id = Column(Integer, ForeignKey("players.id"))

    game = relationship("Game", back_populates="turns")
    player = relationship("Player", back_populates="turns")


class Jail(Base):
    __tablename__ = "jail"
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    player_id = Column(Integer, ForeignKey("players.id"))
    turns_in_jail = Column(Integer, default=0)

    player = relationship("Player", back_populates="jail")  # Fixed from 'connect'


class DiceRoll(Base):
    __tablename__ = "dice_rolls"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    value = Column(Integer)

class Board(Base):
    __tablename__ = "board"
    id = Column(Integer, primary_key=True)  
    position = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String)  



Base.metadata.create_all(engine)

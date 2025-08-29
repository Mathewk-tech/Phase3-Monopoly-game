from sqlalchemy.orm import sessionmaker
from tables import Player, Property
from engine import engine
Session = sessionmaker(bind=engine)
session = Session()

def can_buy_property(player, property):
    if property.owner_id is not None:
        print(f"{property.name}is already owned by {player.name} and cannot be bought")
        return False
    if player.money < property.price:
        print("You have insufficient funds to buy this property")
        return False
    return True


def buy_property(player, property):
   
    if can_buy_property(player, property):
        player.money -= property.price
        property.owner_id = player.id
        session.commit()
        return True
    else:
        return False

def pay_rent(player, property):
    if property.owner_id is None or property.owner_id == player.id:        
        return True
    
    owner = session.query(Player).filter_by(id=property.owner_id).first()
    rent_amount = property.rent
    
    if player.money >= rent_amount:
        player.money -= rent_amount
        owner.money += rent_amount
        session.commit()
        return True
    else:
        return False

def handle_player_landing(player):
    property = session.query(Property).filter_by(position=player.position).first()
    if property is None:
        return
    
    if property.owner_id is None:
        if (player.laps or 0) >= 1:
            pass
    else:
        can_pay = pay_rent(player, property)
        if not can_pay:
            session.delete(player)
            session.commit()

import classes
import rendering


def initialize_game():
    # create player +ships + settlements.

    global player_1
    player_1 = classes.Player(
        name="player_1", npc=0, coin=100, ships=[], settlements=[]
    )

    global tortuga
    tortuga = classes.Settlement(
        position=[600, 300],
        name="Tortuga",
        population=10,
        spice_production=1,
        wood_production=1,
        owner=player_1,
    )

    global florida_keyes
    florida_keyes = classes.Settlement(
        position=[23, 28],
        name="Florida Keyes",
        population=10,
        spice_production=1,
        wood_production=2,
        owner=player_1,
    )

    global havana
    havana = classes.Settlement(
        position=[230, 608],
        name="Havana",
        population=10,
        spice_production=10,
        wood_production=1,
        owner=player_1,
    )

    # global settlement_list
    # settlement_list = [tortuga,florida_keyes,havana]

    global ship_1
    ship_1 = classes.Ship(
        position=[10, 2],
        wood_cargo=0,
        spice_cargo=0,
        destination=[60, 60],
        destination_port=None,
        home_port=tortuga,
        owner=player_1,
    )

    # global ship_list
    # ship_list = [ship_1]

    player_1.settlements.append(tortuga)
    player_1.ships.append(ship_1)

    # gaia = Player( name = "Gaia", npc = 1,coin = 300,trading_fleet = 10,navy = 0)


#  havana = Settlement((25,25),"Havana", owner=Gaia, npc = 1)global player_1


def update(player):
    # updates every thing for the round.

    for setl in player.settlements:
        setl.update_resources()
        setl.wood_price = setl.stockpile_to_price(setl.wood_stockpile)
        setl.spice_price = setl.stockpile_to_price(setl.spice_stockpile)

    for ship in player.ships:
        ship.update()

import pygame 

SHIP_WIDTH = 30
SHIP_HEIGHT = 30

SETTLEMENT_WIDTH = 30
SETTLEMENT_HEIGHT = 40


class Player:
    def __init__(self, name, npc, coin, ships=[], settlements=[]):
        self.name = name
        self.age = npc  # binary
        self.coin = coin
        self.ships = ships
        self.settlements = settlements


class Settlement:
    def __init__(
        self,
        position,
        name,
        owner: Player,
        population=10,
        spice_production=1,
        wood_production=1,
    ):
        self.name = name
        self.population = population
        self.position = position
        self.spice_production = spice_production
        self.spice_stockpile = 10
        self.spice_price = 0.5
        self.wood_production = wood_production
        self.wood_stockpile = 10
        self.wood_price = 0.5
        self.hitbox = pygame.Rect(
            position[0], position[1], SETTLEMENT_WIDTH, SETTLEMENT_HEIGHT
        )
        self.owner = owner

    def is_clicked(self, event):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            return self
        return None

    def stockpile_to_price(self, stockpile):
        if stockpile == 0:
            return 1
        else:
            return 1 - 1 / stockpile

    def trade(self, other_settlement, amount, resource, ship):
        if ship.position != self.position:
            ship.destination = self.position
            return

        if resource == "spice":
            expected_payout = other_settlement.spice_price * amount
            print(expected_payout)
            if amount > self.spice_stockpile:
                print("not enough resources")
                return
            else:
                ship.spice_cargo += amount
                self.spice_stockpile -= amount
                ship.destination == other_settlement.position

        if resource == "wood":
            expected_payout = other_settlement.spice_price * amount
            if amount > self.wood_stockpile:
                print("not enough resources")
                return
            else:
                ship.wood_cargo += amount
                self.wood_stockpile -= amount
                ship.destination == other_settlement.position

    def update_resources(self):
        self.wood_stockpile = self.wood_stockpile + self.wood_production
        self.spice_stockpile = self.spice_stockpile + self.spice_production


class Ship:
    def __init__(
        self,
        position,
        wood_cargo,
        spice_cargo,
        destination,
        home_port,
        owner: Player,
        destination_port = None,
    ):
        self.position = position
        self.wood_cargo = wood_cargo
        self.spice_cargo = spice_cargo
        self.destination = destination
        self.home_port = home_port
        # self.destination_port = destination_port
        self.owner = owner
        self.hitbox = pygame.Rect(position[0], position[1], SHIP_WIDTH, SHIP_HEIGHT)

    def is_clicked(self, event):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            print("ship clicked")
            return self
        return None

    def update(self):
        if self.position[0] - self.destination[0] > 0:
            self.position[0] -= 1
        if self.position[1] - self.destination[1] > 0:
            self.position[1] -= 1

        if self.position[0] - self.destination[0] < 0:
            self.position[0] += 1
        if self.position[1] - self.destination[1] < 0:
            self.position[1] += 1

        self.hitbox = pygame.Rect(
            self.position[0], self.position[1], SHIP_WIDTH, SHIP_HEIGHT
        )

        try:
            if self.position == self.destination_port.position:
                coin = (
                    self.spice_cargo * self.destination_port.spice_price
                    + self.wood_cargo * self.destination_port.wood_price
                )
                self.owner.coin += coin
                self.spice_cargo = 0
                self.wood_cargo = 0
        except:
            print("destination port ill defined")

        print(self.position)

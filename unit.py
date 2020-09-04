import collections

import terrain
import unit_type
import player


class Unit:
    _tag: str = 'unit'

    _terrain_white_list: list = []
    _attack_for_types: dict = {}
    _attack_on_terrain: dict = {}

    _type: unit_type.UnitType = None

    _attack_range: int = 0
    _base_strength: int = 0
    _base_move_points: int = 0
    _base_health: int = 100

    def __init__(self, owner):
        self.owner = owner
        self.health = self._base_health
        self.move_points = self._base_move_points

    def get_strength_by(self, other_unit, terra):
        return int((self._base_strength +
                    self._attack_for_types.get(other_unit.type, 0) +
                    self._attack_on_terrain.get(terra, 0) +
                    terra.base_strength) * (self.health / self._base_strength))

    def can_unit_move_on(self, terra: type) -> bool:
        return terra in self._terrain_white_list

    def get_tag(self) -> str:
        return self._tag


class LightInfantry(Unit):
    _tag: str = 'light_infantry'
    _terrain_white_list: list = [terrain.Desert, terrain.Plain]

    _attack_on_terrain: dict = {
    }

    _attack_for_types: dict = {
    }

    _type: unit_type.UnitType = unit_type.Infantry

    _attack_range: int = 1
    _base_strength: int = 20
    _base_move_points: int = 2
    _base_health: int = 100


class Knight(Unit):
    _tag: str = 'knight'
    _terrain_white_list: list = [terrain.Desert, terrain.Plain]

    _attack_on_terrain: dict = {
    }

    _attack_for_types: dict = {
    }

    _type: unit_type.UnitType = unit_type.Cavalry

    _attack_range: int = 1
    _base_strength: int = 25
    _base_move_points: int = 3
    _base_health: int = 100


class Canon(Unit):
    _tag: str = 'canon'
    _terrain_white_list: list = [terrain.Desert, terrain.Plain]

    _attack_on_terrain: dict = {
    }

    _attack_for_types: dict = {
    }

    _type: unit_type.UnitType = unit_type.Artillery

    _attack_range: int = 2
    _base_strength: int = 30
    _base_move_points: int = 1
    _base_health: int = 100

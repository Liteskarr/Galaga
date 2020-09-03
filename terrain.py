class Terrain:
    tag: str = 'terrain'
    base_move_cost: int = 1
    base_strength: int = 0


class Sea(Terrain):
    tag: str = 'sea'
    base_move_cost: int = 1
    base_strength: int = 0


class Plain(Terrain):
    tag: str = 'plain'
    base_move_cost: int = 1
    base_strength: int = 0


class Desert(Terrain):
    tag: str = 'desert'
    base_move_cost: int = 1
    base_strength: int = 0

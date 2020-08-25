import pygame

if not pygame.get_init():
    pygame.init()


class UserEvent:
    _free_slots = []
    _last = 1

    def __init__(self):
        if len(UserEvent._free_slots):
            self._number = min(UserEvent._free_slots)
            UserEvent._free_slots.remove(min(UserEvent._free_slots))
        else:
            self._number = UserEvent._last
            UserEvent._last += 1

    def __int__(self):
        return pygame.USEREVENT + self._number

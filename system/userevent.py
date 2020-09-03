import pygame


class UserEvent:
    """
    Wrapper for pygame user event.
    """
    _free_slots = []
    _last = 1

    def __init__(self):
        if len(UserEvent._free_slots):
            self._number = min(UserEvent._free_slots)
            UserEvent._free_slots.remove(min(UserEvent._free_slots))
        else:
            self._number = UserEvent._last
            UserEvent._last += 1

    def __int__(self) -> int:
        """
        Turning into int.
        """
        return pygame.USEREVENT + self._number

    def post(self, message: str) -> None:
        """
        Post this event.
        :param message: message for pygame user event
        """
        event = pygame.event.Event(self, message)
        pygame.event.post(event)

    def timer(self, milliseconds: int):
        """
        Set timer for this.
        :param milliseconds: time.
        """
        pygame.time.set_timer(int(self), milliseconds)

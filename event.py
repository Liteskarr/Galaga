class Event:
    """
    C# event analog.
    Subscriber's role can perform any callable object.
    """
    def __init__(self):
        """
        Constructor.
        """
        self._subscribers = []

    def is_subscriber(self, sub) -> bool:
        """
        Returns True if sub is subscriber of event else False.
        :param sub: Reference to callable object.
        """
        return sub in self._subscribers

    def attach(self, sub) -> None:
        """
        Adds subscriber to event.
        :param sub: Reference to callable object.
        """
        self._subscribers.append(sub)

    def detach(self, sub) -> None:
        """
        Deletes subscriber from event.
        :param sub: Reference to callable object.
        """
        self._subscribers.remove(sub)

    def notify(self, *args, **kwargs) -> None:
        """
        Calls every subscriber with args and kwargs.
        """
        for func in self._subscribers:
            func(*args, **kwargs)

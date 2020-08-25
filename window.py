# This is state machine.
import pygame

from event import Event


if not pygame.get_init():
    pygame.init()

clock = pygame.time.Clock()

window_surface = None
window_size = None
window_title = None

mouse_button_up_event = Event()
mouse_button_down_event = Event()
mouse_motion_event = Event()
keydown_event = Event()
keyup_event = Event()
quit_event = Event()


def set_mode(size: tuple, flags=0) -> pygame.Surface:
    global window_surface, window_size
    window_size = size
    window_surface = pygame.display.set_mode(size, flags)
    return window_surface


def set_title(title: str) -> None:
    global window_title
    window_title = title
    pygame.display.set_caption(title)


def poll_events():
    global quit_event, \
        keyup_event, \
        keydown_event, \
        mouse_motion_event, \
        mouse_button_down_event, \
        mouse_button_up_event

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit_event.notify()
            quit(0)
        elif e.type == pygame.MOUSEBUTTONUP:
            mouse_button_up_event.notify(e.pos, e.button)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_down_event.notify(e.pos, e.button)
        elif e.type == pygame.MOUSEMOTION:
            mouse_motion_event.notify(e.pos, e.rel, e.buttons)
        elif e.type == pygame.KEYUP:
            keyup_event.notify(e.key, e.mod)
        elif e.type == pygame.KEYDOWN:
            keydown_event.notify(e.unicode, e.key, e.mod)


def clear(color: tuple = (255, 255, 255)) -> None:
    global window_surface
    window_surface.fill(color)


def update(framerate=0) -> None:
    global clock
    pygame.display.update()
    clock.tick(framerate)


def get_elapsed_time() -> float:
    global clock
    return clock.get_time() / 1000


set_title('Window')

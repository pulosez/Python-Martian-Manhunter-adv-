"""
4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.
"""

from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPlaptop(Laptop):
    def __init__(self, screen_hp, keyboard_hp, touchpad_hp, webcam_hp, port_hp, dynamics_hp):
        self.screen_hp = screen_hp
        self.keyboard_hp = keyboard_hp
        self.touchpad_hp = touchpad_hp
        self.webcam_hp = webcam_hp
        self.port_hp = port_hp
        self.dynamics_hp = dynamics_hp

    def screen(self):
        print(f'Screen: {self.screen_hp}')

    def keyboard(self):
        print(f'Keyboard language: {self.keyboard_hp}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_hp}')

    def webcam(self):
        print(f'Webcam: {self.webcam_hp}')

    def ports(self):
        print(f'Ports: {self.port_hp}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_hp}')


hp_Pavilion = HPlaptop('17.3 (1920x1080) Full HD', 'EN', 'Touchpad with multi-touch gesture support',
                       'TrueVision', '1 x USB 3.1 Type C / 3 x USB 3.1 Type-A / HDMI / LAN (RJ-45)',
                       'HP Audio Boost')
hp_Pavilion.screen()
hp_Pavilion.keyboard()
hp_Pavilion.touchpad()
hp_Pavilion.webcam()
hp_Pavilion.ports()
hp_Pavilion.dynamics()

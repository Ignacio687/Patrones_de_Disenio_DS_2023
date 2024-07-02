from main.command import *
from main.receiver import *
from main.invoker import *

class Cliente():

    def run(self):
        remote = RemoteControlInvoker()

        living_room_light = LightReceiver()
        thermostat = ThermostatReceiver()

        remote.add_command(LightOnCommand(living_room_light))
        remote.add_command(LightOffCommand(living_room_light))
        remote.add_command(TemperatureControlCommand(thermostat, 23.0))

        remote.press_button()
        print()

        remote.add_command(TemperatureControlCommand(thermostat, 36.0))
        remote.add_command(LightOnCommand(living_room_light))

        remote.press_button()
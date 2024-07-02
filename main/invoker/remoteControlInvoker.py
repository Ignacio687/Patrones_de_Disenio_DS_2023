from main.command import CommandABC

class RemoteControlInvoker():
    def __init__(self):
        self._command: list[CommandABC] = []

    def add_command(self, command: CommandABC):
        self._command.append(command)

    def press_button(self):
        for commandCount in range(0, len(self._command)):
            command = self._command.pop(0)
            command.execute()
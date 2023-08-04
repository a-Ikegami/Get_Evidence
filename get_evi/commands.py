import json

class Commands:
    commands: any

    def __init__(self) -> None:
        try:
            with open('commands.json') as commands_file:
                commands = json.load(commands_file)
                self.commands = commands
        except FileExistsError as e:
            print(e)
            return


    def get(self, name) -> list:
        return self.commands[name]

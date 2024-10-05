from core import Engine

class Shell:
    def __init__(self, engine: Engine):
        self.engine = engine

    def run(self):
        while True:
            command = input("Union Search Engine>> ")
            if command == "exit":
                break
            elif command == "showTable":
                print(self.engine.keyword_table.table)
            elif command.startswith("search"):
                query = command.split()[1]
                results = self.engine.search(query)
                for result in results:
                    print(result)
            elif command.startswith("add"):
                url = command.split()[1]
                self.engine.add(url)
            else:
                print("Command not recognized.")
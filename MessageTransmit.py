class PostMistress():
    '''PostMistress class reads, processes and sends messages to respective kingdoms.'''

    def __init__(self, input_file_name, kingdom_list) -> None:
        self.input_file_name = input_file_name
        self.kingdom_list = kingdom_list
        self.delivery_list = []
        self.delivery_dict = {}
        self.processMessage()
        self.deliveryMessage()

    def processMessage(self):
        with open(self.input_file_name, "r") as input_file:
            line_list = input_file.readlines()

        for line in line_list:
            first_space_index = line.find(" ")
            kingdom_name = line[:first_space_index]
            message = line[first_space_index:].replace(" ", "").strip().upper()
            for kingdom in self.kingdom_list:
                if kingdom_name == kingdom.getKingdomName():
                    self.delivery_list.append(kingdom)
            self.delivery_dict[kingdom_name] = message

    def deliveryMessage(self):
        for kingdom in self.delivery_list:
            kingdom_name = kingdom.getKingdomName()
            kingdom.postBox(self.delivery_dict[kingdom_name])
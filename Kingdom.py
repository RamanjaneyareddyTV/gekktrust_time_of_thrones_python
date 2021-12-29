from Cipher import decipher


class Kingdom():
    '''Kingdome class stores kingdom name, emblem, ally status; recieve and process messages.'''

    def __init__(self, kingdom_name, emblem_, list_of_allies) -> None:
        self.kingdom_name = kingdom_name
        self.emblem_ = emblem_.upper()
        self.alliance_list = list_of_allies

    def getKingdomName(self):
        return(self.kingdom_name)

    def postBox(self, message):
        deciphered_message = decipher(message, self.emblem_)
        self.allyDecision(deciphered_message)

    def allyDecision(self, message):
        ally = True
        for a_character_in_emblem in self.emblem_:
            ally &= (self.emblem_.count(a_character_in_emblem) <=
                     message.count(a_character_in_emblem))
        if ally:
            self.alliance_list.joinAlliance(self.kingdom_name)
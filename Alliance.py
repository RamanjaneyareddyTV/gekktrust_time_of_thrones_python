class Alliance():
    '''Stores a list of current alliances and generate alliance report.'''

    def __init__(self) -> None:
        self.alliance_list = []

    def joinAlliance(self, kingdom_name):
        if not(kingdom_name in self.alliance_list):
            self.alliance_list.append(kingdom_name)

    def getAllianceReport(self):
        if len(self.alliance_list) < 3:
            return("NONE")
        else:
            return(f'SPACE {" ".join(self.alliance_list)}')
            
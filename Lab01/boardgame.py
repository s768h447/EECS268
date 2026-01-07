#Sam Harrison 1/26/2022

class BoardGame:

    def __init__(self, name, year_published, gibbons_rating, peoples_rating, min_players, min_playtime):

        self.name = name

        self.year_published = year_published

        self.gibbons_rating = gibbons_rating

        self.peoples_rating = peoples_rating

        self.min_players = min_players

        self.min_playtime = min_playtime

    def __str__(self):

        return (f'{self.name} ({self.year_published}) [GR = {self.gibbons_rating}, ' \
               f'PR = {self.peoples_rating}, MP = {self.min_players}, MT = {self.min_playtime}]')
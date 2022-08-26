############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
    

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType(code='musk', first_harvest=1998, color='green', is_seedless=True, is_bestseller=True, name='Muskmelon')
    muskmelon.add_pairing('mint')

    casaba = MelonType(code='cas', first_harvest=2003, color='orange', is_seedless=False, is_bestseller=False, name='Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('prosciutto')

    yellow_watermelon = MelonType('yw', 2013, 'yellow', True, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
    
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print("")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}

    for melon in melon_types:
        melon_codes[melon.code] = melon

    return melon_codes



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(
        self, melon_type, shape_rating, color_rating, harvested_field, harvested_by, melon_number
    ):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvested_field
        self.harvested_by = harvested_by
        self.melon_number = melon_number

    def __repr__(self):
        return f'{self.name}'

    def is_sellable(self):
        """
        Return True or False if Melon is sellable
          shape_rating must be greater than 5
          color_rating must be greater than 5
          cannot be from field 3
        """
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest


# Muskmelon = MelonType('musk', '1998', 'green', 'seedless', True, 'Muskmelon')

# Muskmelon.update_code('musky')
# print(make_melon_types())
# print(make_melon_type_lookup(make_melon_types()))

# melon9 = Melon('yw', 7, 10, 3, 'Sheila', 'Melon 9')
# print(melon9.is_sellable())

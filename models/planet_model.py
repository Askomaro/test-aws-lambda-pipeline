from datetime import date


class PlanetModel:
    def __init__(self,
                 name: str,
                 rotation_period: int,
                 diameter: str,
                 climate: str,
                 surface_water: int,
                 population: str,
                 created_at: date):
        self.name = name
        self.rotation_period = rotation_period
        self.diameter = diameter
        self.climate = climate
        self.surface_water = surface_water
        self.population = population
        self.created_at = created_at

    def __eq__(self, other):
        if isinstance(other, PlanetModel):
            return (self.name == other.name and
                    self.rotation_period == other.rotation_period and
                    self.diameter == other.diameter and
                    self.climate == other.climate and
                    self.surface_water == other.surface_water and
                    self.population == other.population and
                    self.created_at == other.created_at)

        return False

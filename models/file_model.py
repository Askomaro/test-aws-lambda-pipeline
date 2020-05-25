import os

from helpers.parsers import get_json_from_s3_obj, get_json_val_or_none
from models.planet_model import PlanetModel


class FileModel:
    def __init__(self, s3_file_obj):
        file_path = s3_file_obj.key
        base = os.path.basename(file_path)

        print(f'file path: {base}')
        self.name = os.path.splitext(base)[0]
        self.extension: str = os.path.splitext(base)[1]
        self.planet_models: [PlanetModel] = None
        self.error_msg = None
        self.error_code = None

        json_content = get_json_from_s3_obj(s3_file_obj)

        if 'error' in json_content:
            self.error_msg = json_content['error']
            self.error_code = int(json_content['code'])
        else:
            self.planet_models: [PlanetModel] = self._parse_to_planets_model(json_content)

    def __eq__(self, other):
        if isinstance(other, FileModel):
            return (self.name == other.name and
                    self.extension == other.extension and
                    self.planet_models == other.planet_models and
                    self.error_msg == other.error_msg and
                    self.error_code == other.error_code)

        return False

    def _parse_to_planets_model(self, json_content):
        result = []
        if 'planets' not in json_content:
            result.append(self._match_planet_fields(json_content))
        else:
            for planet_json in json_content['planets']:
                result.append(self._match_planet_fields(planet_json))

        return result

    def _match_planet_fields(self, planet_json):
        # TODO: there is a bug: expected field to be named as 'created_at' but currently there is 'created'
        # in order to have a chance to proceed with testing we assume field 'created'
        # as soon as a bug will be fixed, expected field must be - 'created_at'
        return PlanetModel(
            name=get_json_val_or_none(planet_json, 'name'),
            rotation_period=get_json_val_or_none(planet_json, 'rotation_period'),
            diameter=get_json_val_or_none(planet_json, 'diameter'),
            climate=get_json_val_or_none(planet_json, 'climate'),
            surface_water=get_json_val_or_none(planet_json, 'surface_water'),
            population=get_json_val_or_none(planet_json, 'population'),
            created_at=get_json_val_or_none(planet_json, 'created')
        )

import pytest

from config.config import Config
from core.planet_pipeline import PlanetPipeline


@pytest.yield_fixture(scope='module')
def planet_pipeline():
    print('creating PlanetPipeline object')
    pp = PlanetPipeline()

    yield pp

    print('\ntear down:')
    if Config['delete_files_after_test_running']:
        print('deleting all created files during test execution:')
        pp.delete_all_files()

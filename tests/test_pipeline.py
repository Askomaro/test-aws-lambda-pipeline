import pytest

from core.planet_pipeline import PlanetPipeline
from helpers import generator
from helpers.parsers import extract_date_time_from_str
from helpers.time_execution import print_time_execution
from helpers.validations import validate_iso8601, validate_default_datetime


@print_time_execution
def test__planet_created_at_in_iso_format(planet_pipeline):
    # arrange
    file_name = generator.ger_str()
    payload = {'id': 2}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    file_model = planet_pipeline.get_result_model(file_name)

    # assert
    assert validate_iso8601(file_model.planet_models[0].created_at)


@print_time_execution
def test__empty_payload_returns_all_planet(planet_pipeline):
    # arrange
    file_name = generator.ger_str()
    empty_payload = {}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', empty_payload)
    file_model = planet_pipeline.get_result_model(file_name)

    # assert
    expected_planet_count = 10
    assert len(file_model.planet_models) == expected_planet_count


@print_time_execution
@pytest.mark.parametrize('planet_id', range(1, 11))
def test__contract_values_name(planet_pipeline: PlanetPipeline, planet_id):
    # arrange
    file_name = generator.ger_str()
    payload = {'id': planet_id}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    json_model = planet_pipeline.get_result_json(file_name)

    # assert
    assert 'name' in json_model
    assert 'rotation_period' in json_model
    assert 'diameter' in json_model
    assert 'climate' in json_model
    assert 'surface_water' in json_model
    assert 'population' in json_model
    assert 'created_at' in json_model


@print_time_execution
@pytest.mark.parametrize('planet_id', range(1, 11))
def test__contract_values_type(planet_pipeline: PlanetPipeline, planet_id):
    # arrange
    file_name = generator.ger_str()
    payload = {'id': planet_id}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    json_model = planet_pipeline.get_result_json(file_name)

    # assert
    assert type(json_model['name']) == str, 'field name: "name"'
    assert type(json_model['rotation_period']) == int, 'field name: "rotation_period"'
    assert type(json_model['diameter']) == str, 'field name: "diameter"'
    assert type(json_model['climate']) == str, 'field name: "climate"'
    assert type(json_model['surface_water']) == int, 'field name: "surface_water"'
    assert type(json_model['population']) == str, 'field name: "population"'
    assert type(json_model['created']) == str, 'field name: "created"'


@print_time_execution
@pytest.mark.parametrize('planet_id', range(1, 11))
def test__contract_values_are_valid_and_not_empty(planet_pipeline: PlanetPipeline, planet_id):
    # arrange
    file_name = generator.ger_str()
    payload = {'id': planet_id}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    json_model = planet_pipeline.get_result_json(file_name)

    # assert
    assert json_model['name'] and json_model['name'] != 'unknown', \
        '"name" is empty or unknown or None'
    assert json_model['rotation_period'] and json_model['rotation_period'] != 'unknown', \
        '"rotation_period" is empty or unknown or None'
    assert json_model['diameter'] and json_model['diameter'] != 'unknown', \
        '"diameter" is empty or unknown or None'
    assert json_model['climate'] and json_model['climate'] != 'unknown', \
        '"climate" is empty or unknown or None'
    assert json_model['surface_water'] and json_model['surface_water'] != 'unknown', \
        '"surface_water" is empty or unknown or None'
    assert json_model['population'] and json_model['population'] != 'unknown', \
        '"population" is empty or unknown or None'
    assert json_model['created'] and json_model['created'] != 'unknown', \
        '"created" is empty or unknown or None'


@print_time_execution
def test__same_payload_returns_same_results(planet_pipeline: PlanetPipeline):
    # arrange
    file_name1 = generator.ger_str()
    file_name2 = generator.ger_str()
    payload = {'id': 4}

    # act
    planet_pipeline.put_payload(f'{file_name1}.json', payload)
    planet_pipeline.put_payload(f'{file_name2}.json', payload)
    planet_models1 = planet_pipeline.get_result_model(file_name1).planet_models
    planet_models2 = planet_pipeline.get_result_model(file_name1).planet_models

    # assert
    assert planet_models1 == planet_models2, 'results are not equal when using the same payloads'


@print_time_execution
def test__wrong_planet_id_returns_error(planet_pipeline: PlanetPipeline):
    # arrange
    file_name = generator.ger_str()
    payload = {'id': 20}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    file_model = planet_pipeline.get_result_model(file_name)

    # assert
    assert not file_model.planet_models, 'results are not empty'
    assert file_model.error_msg == 'The planet id is incorrect', 'different error messages'
    assert file_model.error_code == 404, 'different error codes'


@print_time_execution
def test__incorrect_payload_returns_error(planet_pipeline: PlanetPipeline):
    # arrange
    file_name = generator.ger_str()
    payload = {'id_test': '43'}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    file_model = planet_pipeline.get_result_model(file_name)

    # assert
    assert not file_model.planet_models, 'results are not empty'
    assert file_model.error_msg == 'Invalid payload format', 'different error messages'
    assert file_model.error_code == 304, 'different error codes'


@print_time_execution
@pytest.mark.parametrize('planet_id', range(1, 11))
def test__result_files_have_json_extension(planet_pipeline: PlanetPipeline, planet_id):
    # arrange
    file_name = generator.ger_str()
    payload = {'id': planet_id}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    json_model = planet_pipeline.get_result_model(file_name)

    # assert
    assert json_model.extension == '.json'


@print_time_execution
def test__result_file_name_contains_date_time(planet_pipeline: PlanetPipeline):
    # arrange
    file_name = generator.ger_str()
    payload = {'id': 2}

    # act
    planet_pipeline.put_payload(f'{file_name}.json', payload)
    json_model = planet_pipeline.get_result_model(file_name)
    date_time_from_filename = extract_date_time_from_str(json_model.name)

    # assert
    assert validate_default_datetime(date_time_from_filename), 'Incorrect data format, should be YYYY-MM-DD-hh:mm:ss'

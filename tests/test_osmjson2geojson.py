from osmjson2geojson import convert
import json

def test_possible_to_run_process():
    convert({})

def test_no_osmjson_elements():
    osmjson = """{
        "version": 0.6,
        "generator": "Overpass API 0.7.56.6 474850e8",
        "osm3s": {
            "timestamp_osm_base": "2020-10-24T07:21:02Z",
            "timestamp_areas_base": "2020-10-24T06:32:03Z",
            "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL."
        },
        "elements": [

        ]
    }"""

    geojson = """
    {
        "type": "FeatureCollection",
        "generator": "overpass-ide",
        "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.",
        "timestamp": "2020-10-24T07:21:02Z",
        "features": []
    }"""

    assert convert(json.loads(osmjson)) == json.loads(geojson)

def test_one_osmjson_point_element():
    with open("tests/kirseberg.json", "r") as osmjson_file:
        osmjson = json.load(osmjson_file)

    with open("tests/kirseberg.geojson", "r") as geojson_file:
        geojson = json.load(geojson_file)

    assert convert(osmjson) == geojson

def test_malmo_osmjson_point_element():
    with open("tests/malmo.json", "r") as osmjson_file:
        osmjson = json.load(osmjson_file)

    with open("tests/malmo.geojson", "r") as geojson_file:
        geojson = json.load(geojson_file)

    assert convert(osmjson) == geojson
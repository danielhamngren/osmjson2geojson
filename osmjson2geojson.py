__VERSION__ = '0.0.1.dev1'

def convert(osmjson):

    result_dict = {'type': 'FeatureCollection'}

    if "generator" in osmjson:
        result_dict["generator"] = "overpass-ide"  # I want to be identical to turbopass geojson export

    if "osm3s" in osmjson:
        if "copyright" in osmjson["osm3s"]:
            result_dict["copyright"] = osmjson["osm3s"]["copyright"]

        if "timestamp_osm_base" in osmjson["osm3s"]:
            result_dict["timestamp"] = osmjson["osm3s"]["timestamp_osm_base"]

    if "elements" in osmjson:
        features = convert_elements(osmjson["elements"])
        result_dict['features'] = features

    return result_dict


def convert_elements(elements):
    ways = convert_ways_with_center(elements)
    nodes = convert_nodes(elements)

    return ways + nodes


def convert_nodes(elements):
    features = []
    for element in elements:
        if element['type'] == 'node':
            coordinates = [element['lon'], element['lat']]
            feature = create_point_feature(element, coordinates)
            features.append(feature)
    return features


def convert_ways_with_center(elements):
    features = []
    for element in elements:
        if element['type'] == 'way' and 'center' in element:
            coordinates = [element['center']['lon'], element['center']['lat']]
            element['tags']['@geometry'] = 'center'

            feature = create_point_feature(element, coordinates)

            features.append(feature)
    return features


def create_point_feature(element, coordinates):
    return {
        'type': 'Feature',
        'id': f"{element['type']}/{element['id']}",
        'properties': {'@id': f"{element['type']}/{element['id']}", **element['tags']},
        'geometry': {
            'coordinates': coordinates,
            'type': 'Point',
        }
    }

from setuptools import setup

setup(
    name='osmjson2geojson',
    version='0.0.1.dev1',
    description='Converts OSM json from Overpass API to geojson.',
    url='https://github.com/pypa/sampleproject',
    author='Daniel Hamngren',
    author_email='daniel.hamngren@gmail.com',
    python_requires='>=3.7',
    extras_require = {
            'test': ['pytest'],
        },
)

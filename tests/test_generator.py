"""Generate tests."""

import os
import shutil

import pytest

from src import root
from src.generator import generate_app, generate_code

name = 'test'
app_path = os.path.join(root, 'tmp')

def test_generate_app():
    assert os.path.exists(os.path.join(app_path,name))

def test_generate_scaffold(s_name = 'sf1'):
    generate_code(['scaffold','sf1','arg0:string','arg1:string'])
    assert os.path.exists(os.path.join(app_path, name, 'controllers','{}.py'.format(s_name)))
    assert os.path.exists(os.path.join(app_path,name, 'helpers','{}.py'.format(s_name)))
    assert os.path.exists(os.path.join(app_path,name,'templates','sf1s.html'))
    assert os.path.exists(os.path.join(app_path,name, 'models','{}.py'.format(s_name)))
    with open(os.path.join(app_path, name,'routes.py')) as routes:
        assert len([x for x in routes.readlines() if 'sf1' in x]) > 0
        routes.close()

def test_generate_controller():
    generate_code(['controller','tests','arg0:string','arg1:string'])
    assert os.path.exists(os.path.join(app_path, name, 'controllers','{}.py'.format(name)))

def test_generate_helper():
    generate_code(['helper','tests','arg0:string','arg1:string'])
    assert os.path.exists(os.path.join(app_path,name, 'helpers','{}.py'.format(name)))

def test_generate_html():
    generate_code(['view','page','arg0:string','arg1:string'])
    assert os.path.exists(os.path.join(app_path,name,'templates','pages.html'))

def test_generate_model():
    generate_code(['model','tests','arg0:string','arg1:string'])
    assert os.path.exists(os.path.join(app_path,name, 'models','{}.py'.format(name)))

def test_generate_routes():
    generate_code(['controller','route','arg0:string','arg1:string'])
    with open(os.path.join(app_path, name,'routes.py')) as routes:
        assert len([x for x in routes.readlines() if 'route' in x]) > 0
        routes.close()

@pytest.fixture(autouse=True)
def test_setup():

    if not os.path.exists(app_path):
        os.mkdir('tmp')
    os.chdir(app_path)
    generate_app(name)
    os.chdir(os.path.join(app_path, name))
    yield
    os.chdir(root)
    shutil.rmtree(app_path)

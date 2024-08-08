"""Destroy Tests."""
import os

import pytest

from src import root
from src.destroyer import destroy_code
from src.generator import generate_app, generate_code

name = 'test'
s_name = 'sf1'
app_path = os.path.join(root, 'tmp')

def test_destroy_controller():
    assert os.path.exists(os.path.join(app_path,name, 'controllers','{}.py'.format(s_name)))
    destroy_code('controller',s_name)
    assert not os.path.exists(os.path.join(app_path,name, 'controllers','{}.py'.format(s_name)))
    with open(os.path.join(app_path, name,'routes.py')) as routes:
        print(routes.readlines())
        assert len([x for x in routes.readlines() if 'sf1' in x]) == 0
        routes.close()

def test_destroy_helper():
    assert os.path.exists(os.path.join(app_path,name, 'helpers','{}.py'.format(s_name)))
    destroy_code('helper',s_name)
    assert not os.path.exists(os.path.join(app_path,name, 'helpers','{}.py'.format(s_name)))

def test_destroy_model():
    assert os.path.exists(os.path.join(app_path,name, 'models','{}.py'.format(s_name)))
    destroy_code('model', s_name)
    assert not os.path.exists(os.path.join(app_path,name, 'models','{}.py'.format(s_name)))

def test_destroy_html():
    assert os.path.exists(os.path.join(app_path,name, 'templates','sf1s.html'))
    destroy_code('view', s_name)
    assert not os.path.exists(os.path.join(app_path,name, 'models','sf1s.html'))

def test_destroy_scaffold():
    s_name = 'sf1'
    assert os.path.exists(os.path.join(app_path, name, 'controllers','{}.py'.format(s_name)))
    assert os.path.exists(os.path.join(app_path,name, 'helpers','{}.py'.format(s_name)))
    assert os.path.exists(os.path.join(app_path,name,'templates','sf1s.html'))
    assert os.path.exists(os.path.join(app_path,name, 'models','{}.py'.format(s_name)))
    destroy_code('scaffold',s_name)
    assert not os.path.exists(os.path.join(app_path, name, 'controllers','{}.py'.format(s_name)))
    assert not os.path.exists(os.path.join(app_path,name, 'helpers','{}.py'.format(s_name)))
    assert not os.path.exists(os.path.join(app_path,name,'templates','sf1s.html'))
    assert not os.path.exists(os.path.join(app_path,name, 'models','{}.py'.format(s_name)))
    with open(os.path.join(app_path, name,'routes.py')) as routes:
        assert len([x for x in routes.readlines() if 'sf1' in x]) == 0
        routes.close()

@pytest.fixture(autouse=True)
def test_setup():

    if not os.path.exists(app_path):
        os.mkdir('tmp')
    os.chdir(app_path)
    generate_app(name)
    os.chdir(os.path.join(app_path, name))
    generate_code(['scaffold','sf1','arg0:string','arg1:string'])
    yield

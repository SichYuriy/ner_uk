from invoke import task
import subprocess


@task
def build():
    subprocess.check_call('python -m venv venv')
    subprocess.check_call('./venv/Scripts/pip install -r requirements.txt')


@task
def run():
    subprocess.check_call('./venv/Scripts/python main.py')
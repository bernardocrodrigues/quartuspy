from os import getenv
from .exceptions import EnvironmentNotDefined
from shutil import which

necessary_commands = ['quartus']
necessary_env_var = ['QUARTUS_ROOTDIR']

def check_env():

    if(any(which(item) == None for item in necessary_commands)):
        raise EnvironmentNotDefined

    if(any(getenv(item) == None for item in necessary_env_var)):
        raise EnvironmentNotDefined


def main():
    print("Hello World from pyquartus!")



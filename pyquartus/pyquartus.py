from os import getenv
from .exceptions import EnvironmentNotDefined
from shutil import which
from subprocess import run, DEVNULL

necessary_commands = ['quartus_sh']
necessary_env_var = ['QUARTUS_ROOTDIR']


class TclScript(object):

    def __init__(self):
        self.script_array = []

    def puts(self, arg):
        self.script_array.append("puts")
        self.script_array.append(arg)
        self.script_array.append(";")

    def project_new(self, family:str = None, overwrite:bool = False, part:str = None, revision_name:str = None, project_name:str = None):
        self.script_array.append("project_new")

        if family:
            self.script_array.append("-family")
            self.script_array.append(family)

        if overwrite:
            self.script_array.append("-overwrite")

        if part:
            self.script_array.append("-part")
            self.script_array.append(part)

        if revision_name:
            self.script_array.append("-revision_name")
            self.script_array.append(revision_name)

        if project_name:
            self.script_array.append(project_name)

        self.script_array.append(";")

    def set_global_assignment(self, comment:str = None, disable:bool = False, entity_name:str = None, name:str = None, remove:bool = False, section_id:str = None, tag:str = None, value:str = None):
        self.script_array.append("set_global_assignment")

        if comment:
            self.script_array.append("-comment")
            self.script_array.append(comment)

        if disable:
            self.script_array.append("-disable")

        if entity_name:
            self.script_array.append("-entity")
            self.script_array.append(entity_name)

        if name:
            self.script_array.append("-name")
            self.script_array.append(name)

        if remove:
            self.script_array.append("-remove")

        if section_id:
            self.script_array.append("-section_id")
            self.script_array.append(section_id)

        if tag:
            self.script_array.append("-tag")
            self.script_array.append(tag)

        if value:
            self.script_array.append(value)

        self.script_array.append(";")

def check_env():

    if(any(which(item) == None for item in necessary_commands)):
        raise EnvironmentNotDefined

    if(any(getenv(item) == None for item in necessary_env_var)):
        raise EnvironmentNotDefined


def main():
    print("Hello World from pyquartus!")


def call_tcl(script:TclScript):
    result = run(
        ['quartus_sh', '--tcl_eval'] + script.script_array,
        capture_output=True
        # stdout=DEVNULL
    )

    if result.returncode != 0:
        print(result.stderr)

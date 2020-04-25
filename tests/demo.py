
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
import pyquartus


script = pyquartus.TclScript()

script.puts("Hello")
script.puts("World!")

script.project_new(project_name="buba", overwrite=True)
script.set_global_assignment(comment="aaaaa", name="banana", value="eta")

pyquartus.call_tcl(script)


# print(123)
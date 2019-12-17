
import os
import sys
import pytest
from mock import Mock, PropertyMock
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
import pyquartus


def test_pyquartus():

    pyquartus.main()
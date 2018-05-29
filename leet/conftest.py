import importlib.machinery
import os

import pytest


@pytest.fixture()
def s(request):
    file = request.node.fspath.strpath
    name, _ = os.path.basename(file).split('.')
    return importlib.machinery.SourceFileLoader(name, file).load_module().Solution()

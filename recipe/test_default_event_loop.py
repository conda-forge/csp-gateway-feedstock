import asyncio
import importlib
from importlib.metadata import requires
import sys

from packaging.requirements import Requirement


sys.modules["uvloop"] = None
policy = asyncio.get_event_loop_policy()
importlib.import_module("csp_gateway.server.modules.web.perspective")
assert asyncio.get_event_loop_policy() is policy
assert all(Requirement(requirement).name != "uvloop" for requirement in requires("csp-gateway"))

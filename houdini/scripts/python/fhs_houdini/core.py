import hou
from fhs.core import core
import re


def core_function():
    """Debug Function to check if the core module is getting loaded."""
    core.helloCore("Called from Houdini core")


def create_outs():
    """Create Out Nodes"""
    sel_nodes = hou.selectedNodes()
    for sel_node in sel_nodes:
        button, suffix = hou.ui.readInput(
            f"Output suffix for node {sel_node.path()}", buttons=("Create", "Cancel")
        )
        if button == 0:
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", suffix):
                hou.ui.displayMessage(
                    "You used a wrong naming pattern! \n"
                    "Please start with a letter and then only use letters, digits or underscores!"
                )
                return

            geo_container = sel_node.parent()

            name = f"OUT_{suffix.strip()}"

            new_null = geo_container.createNode("null", name)
            # make black
            new_null.setColor(hou.Color(0, 0, 0))
            # make bulge shape
            new_null.setUserData("nodeshape", "bulge")
            new_null.setInput(0, sel_node)
            new_null.moveToGoodPosition()

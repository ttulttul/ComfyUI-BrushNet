from .brushnet_nodes import BrushNetLoader, BrushNet, BlendInpaint#, TestNode
"""
@author: nullquant
@title: BrushNet
@nickname: BrushName nodes
@description: This repository contains an custom nodes for inpaint using BrushNet and PowerPaint models
"""

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BrushNetLoader": BrushNetLoader,
    "BrushNet": BrushNet,
    "BlendInpaint": BlendInpaint,
#    "TestNode": TestNode,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "BrushNetLoader": "BrushNet Loader",
    "BrushNet": "BrushNet",
    "BlendInpaint": "Blend Inpaint",
#    "TestNode": "Test Node",
}

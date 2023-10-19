# -*- coding: utf-8 -*-

# import
from Autodesk.Revit.DB import *

# VARIABLE
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

def get_selected_elements(uidoc):
    return [uidoc.Document.GetElement(elem_id) for elem_id in uidoc.Selection.GetElementIds()]

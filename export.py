# thanks to https://gist.github.com/hyOzd/2e75a9816cfabeb5b4aa

import FreeCAD
import Part

FreeCAD.loadFile("bepis_shell_1.FCStd")

doc = FreeCAD.activeDocument()
base_filename = os.path.splitext(doc.FileName)[0]

objs = []

for o in App.ActiveDocument.Objects:
    if o.Visibility and len(o.InList) == 0: # visible, and top-level
        if not hasattr(o, "Type"):
            print(f"Exporting {o.Label}"); objs.append(o)
        else:
            print(f"Ignoring {o.Label}") # mostly for imported objects like PCB v1 and v2

compound_objs = {'Lid - Sharp LCD frame cover':"Lid"}

for obj in objs:
    # first export all non-compound so that the simplest stuff always succeeds
    if obj.Label not in compound_objs:
        filename = base_filename + "_" + obj.Label + ".stl"
        obj.Shape.exportStl(filename, 1)
        print(f"Exported {filename}")

for obj in objs:
    # now we only work on compound objects
    if obj.Label not in compound_objs:
        continue
    filename = base_filename + "_" + obj.Label + ".stl"
    add_obj_name_start = compound_objs[obj.Label]
    add_obj = None
    for other_obj in objs:
        if other_obj.Label != obj.Label and other_obj.Label.startswith(add_obj_name_start):
            add_obj = other_obj; break
    if add_obj is None:
        print("Cannot find pair object for {obj.Label} ({add_obj_name_start})")
        import sys; sys.exit(1)
    fuse = obj.Shape.fuse(add_obj.Shape)

    ooobj = doc.addObject("Part::Feature", f"{obj.Label}+{add_obj.Label}")
    ooobj.Shape = fuse
    doc.recompute()
    ooobj.Shape.exportStl(filename, 1)
    print(f"Exported {filename}")

sys.exit(0)

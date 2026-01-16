# blepis-case

A 3D printed case designed to fit a Blepis/Beepy board. Files provided are in FreeCAD (actual source files, not STL).

## v2.0 - is compatible with Blepis v2, likely all final quality of life features complete!

### Top-level parts in the FreeCAD file:

* `Lid +ears`: top part
* `Lid - Sharp LCD frame cover`: frame to hold the Sharp LCD in place. You should Ctrl+click the two Lid parts to export them together for printing.
* `Back shell +addon holes`: bottom part
* `Left button cover`: lever for buttons. Is perfect for the right-side buttons, and you can print out a second one to temporarily accomodate the left-side buttons
* `Captive-izing screw washer`: a printable nut that friction-fits the four M3*25 screws, so that they don't fall out of their holes. Print four copies. Two at the top fasten the case to the lid, and two at the bottom fasten the lid+board together.
* `microUSB plug`: cover for the microUSB plug needed to make contact with Pi Zero's microUSB data port.
* `Keeb spacer`: a thin flat part that goes under the keyboard to make it flush with top of the lid. Imperfect and to be tweaked soon, but it's pretty helpful already.

Designed for 0.4mm printer nozzle width. In our experience, is best printed at 0.1mm layer height. Few supports expected, most parts are support-less, though the microUSB cover, and M3 nut spots on the back shell, might be a little tricky in that regard; expect to have to clean up these two spots a little after printing. Tree supports should make for perfect prints.

### Battery support:

* two 103395 batteries in parallel ([example](https://www.amazon.de/-/en/dp/B08HQH19KS)), with plenty of room for cell padding
* alternate batteries possible if you mod the case to your liking - can be as simple as tearing out the battery separator, since it's designed to be thin and easy to remove.

### Modding capabilities:

A 46x104mm 4-screw rectangle pattern, expects four threaded inserts for M2.5 screws. Currently available parts:

* A waist clip. See `beepis_waist_1` for v2, complete with lanyard hooks. More upgrades and accessories for it incoming!
* A holder base with holes for two countersunk screws. Incompatible with the waist clip, **deprecated**; see `beepis_holder_base` for v0.

### Required parts:

* 10x10cm 1mm thick foam sheet
* 10x10cm 2mm thick foam sheet
* Thin double-sided tape for attaching the foam sheets
* M3 nuts, metal, 4pcs
* M3x25 screws, countersunk (conical head), metal, 4pcs

Extra parts:

* M2.5 threaded inserts

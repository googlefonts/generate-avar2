


from fontTools import ttLib
from fontTools.varLib.instancer import instantiateVariableFont

#pins = {axis:axes[axis][1] for axis in derived_axes}
#print("Loading AmstelvarAlpha-VF full font")
#font = ttLib.TTFont('AmstelvarAlpha-VF.ttf')
#print("Pinning derived axes")
#instantiateVariableFont(font, pins)

# ~/fonttools/fonttools varLib.instancer AmstelvarAlpha-VF.ttf wdth=100 wght=400 opsz=14

print("Loading AmstelvarAlpha-VF pinned font")
font = ttLib.TTFont('AmstelvarAlpha-VF-partial.ttf')



print("Loading fvar and gvar tables.")
fvar = font['fvar']
gvar = font['gvar']

#print("Hiding source axes in fvar")
#for axis in fvar.axes:
#    axis.flags |= 1

print("Nuking all named instances")
fvar.instances = []
fvar_axes = [ax.axisTag for ax in fvar.axes]

source_axes = fvar_axes[:]
axes = {}
for axis in fvar.axes:
    axes[axis.axisTag] = (axis.minValue,axis.defaultValue,axis.maxValue)

print("Loading AmstelvarAlpha.truevalues")
import xml.etree.ElementTree as ET
tree = ET.parse('AmstelvarAlpha.truevalues')
root = tree.getroot()[0]
derived_axes = []
for axis in root.iter('axis'):
    tag = axis.attrib['name']
    derived_axes.append(tag)
    locations = list(axis.iter('location'))
    assert len(locations) == 3
    locations = tuple(sorted([int(l.attrib['value']) for l in locations]))
    axes[tag] = locations

source_locations = {}
derived_locations = {}
for axis_node in root.iter('axis'):
    for location_node in axis_node.iter('location'):
        axis = axis_node.attrib['name']
        location = int(location_node.attrib['value'])
        key = "%s=%d" % (axis, location)
        derived_locations[key] = {axis: location}

        source_location = {}
        for dimension_node in location_node.iter('dimension'):
            dimension = dimension_node.attrib['name']
            value = int(dimension_node.attrib['xvalue'])
            source_location[dimension] = value

        source_locations[key] = source_location


#del root, axis, tag, l, locations

print("Adding back derived axes to fvar")
for axis in derived_axes:
    if axis in fvar_axes: continue
    Axis = ttLib.getTableModule('fvar').Axis()
    Axis.axisTag = axis
    Axis.minValue = axes[axis][0]
    Axis.defaultValue = axes[axis][1]
    Axis.maxValue = axes[axis][2]
    Axis.flags = 0
    Axis.axisNameID = font['name'].addName(axis)
    fvar.axes.append(Axis)
fvar_axes = [ax.axisTag for ax in fvar.axes]


print("Modeling avar2")
from fontTools.varLib import models
from fontTools.varLib import varStore
from fontTools.ttLib.tables import otTables

source_locations_normalized = {key:models.normalizeLocation(loc, axes) for key,loc in source_locations.items()}
derived_locations_normalized = {key:models.normalizeLocation(loc, axes) for key,loc in derived_locations.items()}

to_delete = set()
for k1,v1 in derived_locations_normalized.items():
    for k2,v2 in derived_locations_normalized.items():
        if k1 == k2 or k2 in to_delete or k1 in to_delete:
            continue
        if v1 == v2:
            assert source_locations_normalized[k1] == source_locations_normalized[k2]
            to_delete.add(k2)
            #print("Duplicate derived locations for %s and %s: %s" % (k1, k2, v1))
            #abort

for k in to_delete:
    del source_locations_normalized[k]
    del derived_locations_normalized[k]

for k1,v1 in source_locations_normalized.items():
    for k2,v2 in source_locations_normalized.items():
        if k1 == k2:
            continue
        if v1 == v2:
            print("Duplicate source locations for %s and %s: %s" % (k1, k2, v1))
            abort

model = models.VariationModel(derived_locations_normalized.values(), list(axes.keys()))
store_builder = varStore.OnlineVarStoreBuilder(axes.keys())
store_builder.setModel(model)
varIdxes = {}
for axis in axes:
    masters = [m.get(axis, 0)*(1<<14) for m in source_locations_normalized.values()]
    varIdxes[axis] = store_builder.storeMasters(masters)[1]
store = store_builder.finish()
mapping = store.optimize()
varIdxes = {axis:mapping[value] for axis,value in varIdxes.items()}
del model, store_builder, mapping

varIdxMap = otTables.VarIdxMap()
varIdxMap.mapping = []
for axis in fvar.axes:
    tag = axis.axisTag
    varIdxMap.mapping.append(varIdxes[tag])

print("Generating avar2")
avar_t = font['avar'] = ttLib.getTableClass('avar')()
avar = avar_t.table = otTables.avar()
avar.Version = 0x00020000
avar.Reserved = 0
segMap = otTables.AxisSegmentMap()
segMap.AxisValueMap = []
avar.AxisSegmentMap = [segMap] * len(fvar_axes)
avar.VarIdxMap = varIdxMap
avar.VarStore = store

print("Saving AmstelvarAlpha-avar2-from-truevalues.ttf")
font.save('AmstelvarAlpha-avar2-from-truevalues.ttf')



axes_str = """\
wght	wght	400	100	1000
wdth	wdth	100	25	151
opsz	opsz	14	8	144
GRAD	GRAD	0	-1	1
slnt	slnt	0	-10	0
XTRA	XTRA	468	323	603
XOPQ	XOPQ	96	27	175
YOPQ	YOPQ	79	25	135
YTLC	YTLC	514	416	570
YTUC	YTUC	712	528	760
YTAS	YTAS	750	649	854
YTDE	YTDE	-203	-305	-98
YTFI	YTFI	738	560	788
"""
axes = {}
for line in axes_str.splitlines():
    fields = line.split()
    axes[fields[0]] = (int(fields[3]), int(fields[2]), int(fields[4]))
del line, fields

measurements_header = """\
Source	UPM	XOPQ	XTRA	GRAD	YOPQ	YTAS	YTDE	YTUC	YTLC	YTFI
"""
measurements_order = measurements_header.split()
source_axes = measurements_order[2:]
derived_axes = [axis for axis in axes.keys() if axis not in source_axes]

measurements_str_commented_out = """\
RobotoFlex-Slant.ufo	2048	186	898	186	158	1536	-416	1456	1052	1456
RobotoFlex-opsz14-wght100-slnt-10.ufo	2048	84	835	84	85	1536	-416	1456	1052	1456
"""
measurements_str = """\
RobotoFlex-Regular.ufo	2048	192	926	192	158	1536	-416	1456	1052	1456
RobotoFlex-GRAD-1.ufo	2048	131	947	131	96	1536	-416	1456	1052	1456
RobotoFlex-GRAD1.ufo	2048	254	895	254	221	1536	-416	1456	1052	1456
RobotoFlex-wght100.ufo	2048	97	972	97	88	1536	-416	1456	1052	1456
RobotoFlex-wght900.ufo	2048	421	860	421	313	1526	-416	1456	1058	1456
RobotoFlex-opsz8.ufo	2048	205	984	205	172	1536	-416	1456	1090	1456
RobotoFlex-opsz144.ufo	2048	110	800	110	98	1458	-444	1456	914	1456
RobotoFlex-wdth25.ufo	2048	184	778	184	154	1536	-416	1456	1052	1456
RobotoFlex-wdth151.ufo	2048	202	1076	202	162	1536	-416	1456	1052	1456
RobotoFlex-XOPQ27.ufo	2048	54	788	54	158	1536	-416	1456	1052	1456
RobotoFlex-XOPQ175.ufo	2048	350	1084	350	158	1536	-416	1456	1052	1456
RobotoFlex-XTRA323.ufo	2048	192	646	192	158	1536	-416	1456	1052	1456
RobotoFlex-XTRA603.ufo	2048	192	1206	192	158	1536	-416	1456	1052	1456
RobotoFlex-YOPQ25.ufo	2048	192	926	192	50	1536	-416	1456	1052	1456
RobotoFlex-YOPQ135.ufo	2048	192	926	192	270	1536	-416	1456	1052	1456
RobotoFlex-YTLC416.ufo	2048	192	926	192	158	1536	-416	1456	852	1456
RobotoFlex-YTLC570.ufo	2048	192	926	192	158	1536	-416	1456	1168	1456
RobotoFlex-YTUC528.ufo	2048	192	926	192	158	1536	-416	1082	1052	1456
RobotoFlex-YTUC760.ufo	2048	192	926	192	158	1536	-416	1556	1052	1456
RobotoFlex-YTAS649.ufo	2048	192	926	192	158	1330	-416	1456	1052	1456
RobotoFlex-YTAS854.ufo	2048	192	926	192	158	1750	-416	1456	1052	1456
RobotoFlex-YTDE-305.ufo	2048	192	926	192	158	1536	-620	1456	1052	1456
RobotoFlex-YTDE-98.ufo	2048	192	926	192	158	1536	-200	1456	1052	1456
RobotoFlex-YTFI560.ufo	2048	192	926	192	158	1536	-416	1456	1052	1090
RobotoFlex-YTFI788.ufo	2048	192	926	192	158	1536	-416	1456	1052	1556
RobotoFlex-opsz144-wdth151.ufo	2048	110	1210	110	98	1456	-416	1456	914	1456
RobotoFlex-opsz144-wdth25.ufo	2048	98	202	98	104	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght900.ufo	2048	600	690	600	499	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght100.ufo	2048	10	860	10	8	1454	-444	1456	914	1456
RobotoFlex-opsz8-wdth151.ufo	2048	215	1133	215	176	1536	-416	1456	1089	1456
RobotoFlex-opsz8-wdth25.ufo	2048	197	836	197	168	1536	-416	1456	1089	1456
RobotoFlex-opsz8-wght900.ufo	2048	322	961	322	228	1536	-416	1456	1116	1456
RobotoFlex-opsz8-wght100.ufo	2048	110	1030	110	101	1536	-416	1456	1089	1456
RobotoFlex-wght900-wdth25.ufo	2048	413	712	413	309	1526	-416	1456	1058	1456
RobotoFlex-opsz144-wght100-wdth151.ufo	2048	10	1270	10	10	1456	-416	1456	914	1455
RobotoFlex-opsz144-wght100-wdth25.ufo	2048	6	144	6	6	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght900-wdth151.ufo	2048	600	1100	600	499	1454	-388	1456	914	1456
RobotoFlex-opsz144-wght900-wdth25.ufo	2048	490	520	490	497	1456	-388	1456	914	1456
RobotoFlex-opsz8-wght900-wdth25.ufo	2048	314	813	314	224	1536	-416	1456	1116	1456
RobotoFlex-opsz144-wght100.ufo	2048	10	860	10	8	1454	-444	1456	914	1456
RobotoFlex-opsz144-wght100-wdth25.ufo	2048	6	144	6	6	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght100-wdth151.ufo	2048	10	1270	10	10	1456	-416	1456	914	1455
RobotoFlex-opsz144-wght100-wdth25.ufo	2048	6	144	6	6	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght100.ufo	2048	10	860	10	8	1454	-444	1456	914	1456
RobotoFlex-opsz144-wght100-wdth25.ufo	2048	6	144	6	6	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght100-wdth151.ufo	2048	10	1270	10	10	1456	-416	1456	914	1455
RobotoFlex-opsz144-wght100-wdth25.ufo	2048	6	144	6	6	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght100.ufo	2048	10	860	10	8	1454	-444	1456	914	1456
RobotoFlex-opsz144-wdth25.ufo	2048	98	202	98	104	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght100-wdth25.ufo	2048	6	144	6	6	1456	-416	1456	914	1456
RobotoFlex-opsz144-wght900-wdth25.ufo	2048	490	520	490	497	1456	-388	1456	914	1456
RobotoFlex-opsz144-wght100-wdth151.ufo	2048	10	1270	10	10	1456	-416	1456	914	1455
RobotoFlex-opsz144-wght100-wdth25.ufo	2048	6	144	6	6	1456	-416	1456	914	1456
"""

"""
RobotoExtremo-opsz144-wght400-wdth100-XOPQ27.ufo	2048	0	-444	748	86	98	0	1900	1456	1456
RobotoExtremo-opsz144-wght100.ufo	2048	0	-444	860	92	8	0	1900	1456	1456
RobotoExtremo-opsz144-wght400-wdth25-XOPQ27.ufo	2048	0	-416	162	42	104	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth25.ufo	2048	0	-416	144	44	6	0	1872	1456	1456
RobotoExtremo-opsz144-wght900-wdth25-XOPQ27.ufo	2048	0	-388	488	6	497	0	1844	1456	1456
RobotoExtremo-opsz144-wght400-wdth151-XOPQ27.ufo	2048	0	-416	1170	86	98	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth151.ufo	2048	0	-416	1270	92	10	0	1872	1456	1455
RobotoExtremo-opsz144-wght900-wdth151-XOPQ27.ufo	2048	0	-388	1032	24	499	0	1844	1456	1456
RobotoExtremo-opsz144-wght400-wdth25-XOPQ175.ufo	2048	0	-416	290	42	104	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth25.ufo	2048	0	-416	144	44	6	0	1872	1456	1456
RobotoExtremo-opsz144-wght900-wdth25-XOPQ175.ufo	2048	0	-388	610	6	497	0	1844	1456	1456
RobotoExtremo-opsz144-wght900-wdth151-XOPQ175.ufo	2048	0	-388	1178	24	499	0	1844	1456	1456
RobotoExtremo-opsz8-wght100-wdth100-YOPQ25.ufo	2048	0	-416	927	115	58	0	1872	1456	1456
RobotoExtremo-opsz8-wght100-wdth25-YOPQ25.ufo	2048	0	-416	779	115	54	0	1872	1456	1456
RobotoExtremo-opsz8-wght100-wdth151-YOPQ25.ufo	2048	0	-416	1077	115	44	0	1872	1456	1456
RobotoExtremo-opsz14-wght100-wdth100-YOPQ25.ufo	2048	0	-416	869	115	33	0	1872	1456	1456
RobotoExtremo-opsz14-wght100-wdth25-YOPQ25.ufo	2048	0	-416	721	115	29	0	1872	1456	1456
RobotoExtremo-opsz14-wght100-wdth151-YOPQ25.ufo	2048	0	-416	1019	115	37	0	1872	1456	1456
RobotoExtremo-opsz144-wght400-wdth100-YOPQ25.ufo	2048	0	-444	800	86	46	0	1900	1456	1456
RobotoExtremo-opsz144-wght100.ufo	2048	0	-444	860	92	8	0	1900	1456	1456
RobotoExtremo-opsz144-wght400-wdth25-YOPQ25.ufo	2048	0	-416	202	42	82	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth25.ufo	2048	0	-416	144	44	6	0	1872	1456	1456
RobotoExtremo-opsz144-wght400-wdth151-YOPQ25.ufo	2048	0	-416	1210	86	76	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth151.ufo	2048	0	-416	1270	92	10	0	1872	1456	1455
RobotoExtremo-opsz144-wght900-wdth151-YOPQ25.ufo	2048	0	-388	1100	24	451	0	1844	1456	1456
RobotoExtremo-opsz144-wght900-wdth100-YOPQ135.ufo	2048	0	-416	690	24	529	0	1872	1456	1456
RobotoExtremo-opsz144-wght400-wdth25-YOPQ135.ufo	2048	0	-416	202	42	134	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth25.ufo	2048	0	-416	144	44	6	0	1872	1456	1456
RobotoExtremo-opsz144-wght900-wdth25-YOPQ135.ufo	2048	0	-388	520	6	519	0	1844	1456	1456
RobotoExtremo-opsz144-wght900-wdth151-YOPQ135.ufo	2048	0	-388	1100	24	533	0	1844	1456	1456
RobotoExtremo-opsz8-wght900-wdth25-XTRA323.ufo	2048	0	-416	608	115	224	0	1872	1456	1456
RobotoExtremo-opsz14-wght900-wdth100-XTRA323.ufo	2048	0	-416	681	84	313	0	1872	1456	1456
RobotoExtremo-opsz14-wght900-wdth25-XTRA323.ufo	2048	0	-416	631	84	309	0	1872	1456	1456
RobotoExtremo-opsz144-wght100.ufo	2048	0	-444	860	92	8	0	1900	1456	1456
RobotoExtremo-opsz144-wght900-wdth100-XTRA323.ufo	2048	0	-416	673	24	499	0	1872	1456	1456
RobotoExtremo-opsz144-wdth25.ufo	2048	0	-416	202	42	104	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth25.ufo	2048	0	-416	144	44	6	0	1872	1456	1456
RobotoExtremo-opsz144-wght900-wdth25.ufo	2048	0	-388	520	6	497	0	1844	1456	1456
RobotoExtremo-opsz144-wght400-wdth100-XTRA323.ufo	2048	0	-444	520	86	102	0	1900	1456	1456
RobotoExtremo-opsz144-wght100-wdth151.ufo	2048	0	-416	1270	92	10	0	1872	1456	1455
RobotoExtremo-opsz144-wght400-wdth151-XTRA323.ufo	2048	0	-416	930	86	98	0	1872	1456	1456
RobotoExtremo-opsz144-wght400-wdth100-XTRA603.ufo	2048	0	-444	1080	86	100	0	1900	1456	1456
RobotoExtremo-opsz144-wght100-wdth100-XTRA603.ufo	2048	0	-444	1140	92	8	0	1900	1456	1456
RobotoExtremo-opsz144-wght400-wdth25-XTRA603.ufo	2048	0	-416	482	42	104	0	1872	1456	1456
RobotoExtremo-opsz144-wght100-wdth25.ufo	2048	0	-416	144	44	6	0	1872	1456	1456
RobotoExtremo-opsz144-wght900-wdth25-XTRA603.ufo	2048	0	-388	545	6	497	0	1844	1456	1456
RobotoExtremo-opsz144-wght100-wdth151-XTRA603.ufo	2048	0	-416	1550	92	10	0	1872	1456	1455
"""
measurements = {}
for line in measurements_str.splitlines():
    fields = line.split()
    it = zip(measurements_order, fields)

    source = fields[0]
    this = measurements[source] = {}

    next(it) # skip Source
    next(it) # skip UPM
    for key,value in it:
        this[key] = int(value)
del line, fields, it, source, this

# Check for duplicates
for k1,v1 in measurements.items():
    for k2,v2 in measurements.items():
        if k1 == k2:
            continue
        if v1 == v2:
            print("Duplicate measurements for %s and %s" % (k1, k2))


import re
derived_locations = {}
for key in measurements.keys():
    values = re.findall(r'-([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])(-?[0-9]+)', key)
    location = derived_locations[key] = {}
    for tag, value in values:
        location[tag] = int(value)
del location, key, values, tag, value


#from pprint import pprint
#pprint(axes)
#pprint(derived_locations)
#pprint(measurements)

from fontTools import ttLib
from fontTools.varLib.instancer import instantiateVariableFont

# ~/fonttools/fonttools varLib.instancer RobotoFlex\[GRAD\,XOPQ\,XTRA\,YOPQ\,YTAS\,YTDE\,YTFI\,YTLC\,YTUC\,opsz\,slnt\,wdth\,wght\].ttf wdth=100 wght=400 opsz=14 slnt=0
pins = {axis:axes[axis][1] for axis in derived_axes}
#print("Loading RobotoFlex full font")
#font = ttLib.TTFont('RobotoFlex[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght].ttf')
#print("Pinning derived axes")
#instantiateVariableFont(font, pins)

print("Loading RobotoFlex pinned font")
font = ttLib.TTFont('RobotoFlex[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght]-partial.ttf')

fvar = font['fvar']

print("Hiding source axes in fvar")
for axis in fvar.axes:
    axis.flags |= 1

print("Nuking all named instances")
fvar.instances = []
print("Adding back derived axes to fvar")
for axis in derived_axes:
    Axis = ttLib.getTableModule('fvar').Axis()
    Axis.axisTag = axis
    Axis.minValue = axes[axis][0]
    Axis.defaultValue = axes[axis][1]
    Axis.maxValue = axes[axis][2]
    Axis.flags = 0
    Axis.axisNameID = font['name'].addName(axis)
    fvar.axes.append(Axis)

"""
# Axes min/default/max seem to need doubling for source axes; doesn't work
new_axes = {}
for tag,value in axes.items():
    if tag in source_axes:
        (min_v,default_v,max_v) = value
        value = (2*min_v, 2*default_v, 2*max_v)
    new_axes[tag] = value
axes = new_axes
del new_axes, value, min_v, default_v, max_v
"""

# Axes min/default/max seem to be wrong. Update manually.
# First measurement is for base master:
orig_axes = axes.copy()
name,default_loc = list(measurements.items())[0]
min_loc = {axis:min(m[axis] for m in measurements.values()) for axis in source_axes}
max_loc = {axis:max(m[axis] for m in measurements.values()) for axis in source_axes}
assert name.find('Regular')
for axis in source_axes:
    axes[axis] = (min_loc[axis], default_loc[axis], max_loc[axis])
del name, axis, default_loc, min_loc, max_loc


print("Modeling avar2")
from fontTools.varLib import models
from fontTools.varLib import varStore
from fontTools.ttLib.tables import otTables

source_locations_normalized = {key:models.normalizeLocation(loc, axes) for key,loc in measurements.items()}
for k1,v1 in source_locations_normalized.items():
    for k2,v2 in source_locations_normalized.items():
        if k1 == k2:
            continue
        if v1 == v2:
            print("Duplicate source locations for %s and %s: %s" % (k1, k2, v1))
            abort
derived_locations_normalized = {key:models.normalizeLocation(loc, orig_axes) for key,loc in derived_locations.items()}
for k1,v1 in derived_locations_normalized.items():
    for k2,v2 in derived_locations_normalized.items():
        if k1 == k2:
            continue
        if v1 == v2:
            print("Duplicate derived locations for %s and %s: %s" % (k1, k2, v1))
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
avar.AxisSegmentMap = []
avar.VarIdxMap = varIdxMap
avar.VarStore = store

font.save('out.ttf')

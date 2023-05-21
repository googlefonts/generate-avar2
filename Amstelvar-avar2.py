from fontTools import ttLib
from fontTools.varLib.instancer import instantiateVariableFont


axes_str = """\
wght	wght	400	100	900
wdth	wdth	100	50	125
opsz	opsz	14	8	144
GRAD	GRAD	0	-1	1
XTRA	XTRA	562	324	640
XOPQ	XOPQ	176	18	263
YOPQ	YOPQ	124	15	132
YTLC	YTLC	500	420	570
YTUC	YTUC	750	500	1000
YTAS	YTAS	767	500	983
YTDE	YTDE	-240	-500	-138
YTFI	YTFI	760	425	1000
"""
axes = {}
for line in axes_str.splitlines():
    fields = line.split('\t')
    axes[fields[0]] = (int(fields[3]), int(fields[2]), int(fields[4]))
del line, fields


measurements_header = """\
Source	UPM	XOPQ	XOPQ ‰	XOUC	XOUC ‰	XOLC	XOLC ‰	XOFI	XOFI ‰	XTRA	XTRA ‰	XTUC	XTUC ‰	XTLC	XTLC ‰	XTFI	XTFI ‰	XTAB	XTAB ‰	GRAD	GRAD ‰	XTSB	XTSB ‰	XUCS	XUCS ‰	XUCR	XUCR ‰	XLCS	XLCS ‰	XLCR	XLCR ‰	XFIR	XFIR ‰	YOPQ	YOPQ ‰	YOUC	YOUC ‰	YOLC	YOLC ‰	YOFI	YOFI ‰	YTAS	YTAS ‰	YTDE	YTDE ‰	YTOS	YTOS ‰	YTUO	YTUO ‰	YTLO	YTLO ‰	YTFO	YTFO ‰	YTDO	YTDO ‰	YTAO	YTAO ‰
"""
measurements_order = measurements_header.split('\t')

"""
Amstelvar-Roman-YTUC500.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1031	516	1031	516	1022	511	1520	760	-518	-259	1537	769
Amstelvar-Roman-YTFI425.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	872	436	-518	-259	1537	769
Amstelvar-Roman-YTLC570.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1167	584	1520	760	-518	-259	1537	769
Amstelvar-Roman-YTLC420.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	863	432	1520	760	-518	-259	1537	769
Amstelvar-Roman-YTUC1000.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	2032	1016	2032	1016	1022	511	1520	760	-518	-259	1537	769
Amstelvar-Roman-YTFI1000.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	2022	1011	-518	-259	1537	769
"""

measurements_str = """\
Amstelvar-Roman.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1537	769
Amstelvar-Roman-GRAD-1.ufo	2000	72	36	72	36	68	34	176	88	981	491	981	491	704	352	711	356	1000	500	72	36	343	172	343	172	100	50	249	125	75	38	52	26	64	32	64	32	51	26	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1537	769
Amstelvar-Roman-GRAD1.ufo	2000	282	141	282	141	255	128	176	88	980	490	980	490	606	303	711	356	1000	500	282	141	239	120	239	120	60	30	206	103	54	27	52	26	144	72	144	72	141	71	130	65	1534	767	-480	-240	1530	765	1530	765	1022	511	1520	760	-518	-259	1537	769
Amstelvar-Roman-wght100.ufo	2000	76	38	76	38	74	37	75	38	1020	510	1020	510	696	348	805	403	1040	520	76	38	318	159	318	159	85	43	256	128	68	34	78	39	54	27	54	27	60	30	64	32	1509	755	-480	-240	1520	760	1520	760	1022	511	1520	760	-510	-255	1514	757
Amstelvar-Roman-wght900.ufo	2000	497	249	497	249	479	240	490	245	1001	501	1001	501	825	413	860	430	1489	745	497	249	222	111	222	111	65	33	183	92	52	26	60	30	154	77	154	77	152	76	151	76	1534	767	-480	-240	1527	764	1527	764	1076	538	1525	763	-496	-248	1532	766
Amstelvar-Roman-opsz8.ufo	2000	220	110	220	110	209	105	219	110	1024	512	1024	512	699	350	628	314	1000	500	220	110	292	146	292	146	80	40	226	113	64	32	74	37	174	87	174	87	159	80	184	92	1534	767	-480	-240	1520	760	1520	760	1072	536	1520	760	-518	-259	1539	770
Amstelvar-Roman-opsz144.ufo	2000	163	82	163	82	149	75	160	80	864	432	864	432	604	302	689	345	971	486	163	82	228	114	228	114	65	33	181	91	48	24	55	28	29	15	29	15	43	22	31	16	1511	756	-460	-230	1519	760	1519	760	942	471	1520	760	-490	-245	1512	756
Amstelvar-Roman-wdth50.ufo	2000	166	83	166	83	155	78	160	80	610	305	610	305	404	202	606	303	910	455	166	83	196	98	196	98	64	32	148	74	50	25	62	31	120	60	120	60	111	56	126	63	1534	767	-480	-240	1520	760	1520	760	1019	510	1520	760	-518	-259	1518	759
Amstelvar-Roman-wdth125.ufo	2000	180	90	180	90	171	86	174	87	1366	683	1366	683	1043	522	1215	608	1580	790	180	90	380	190	380	190	96	48	320	160	90	45	93	47	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1031	516	1520	760	-518	-259	1518	759
Amstelvar-Roman-XOPQ18.ufo	2000	36	18	36	18	36	18	36	18	840	420	840	420	526	263	713	357	916	458	36	18	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1518	759
Amstelvar-Roman-XOPQ263.ufo	2000	526	263	526	263	496	248	510	255	1330	665	1330	665	986	493	1207	604	1904	952	526	263	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1533	767
Amstelvar-Roman-XTRA324.ufo	2000	176	88	176	88	166	83	176	88	649	325	649	325	451	226	595	298	898	449	176	88	292	146	292	146	80	40	226	113	64	32	52	26	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1518	759
Amstelvar-Roman-XTRA640.ufo	2000	176	88	176	88	166	83	176	88	1280	640	1280	640	856	428	911	456	1190	595	176	88	292	146	292	146	80	40	226	113	64	32	52	26	124	62	124	62	111	56	130	65	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1518	759
Amstelvar-Roman-YOPQ15.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	29	15	29	15	21	11	20	10	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1518	759
Amstelvar-Roman-YOPQ132.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	264	132	264	132	181	91	267	134	1534	767	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1518	759
Amstelvar-Roman-YTAS500.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1034	517	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	1185	593
Amstelvar-Roman-YTAS983.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	2000	1000	-480	-240	1520	760	1520	760	1022	511	1520	760	-518	-259	2009	1005
Amstelvar-Roman-YTDE-138.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-276	-138	1520	760	1520	760	1022	511	1520	760	-298	-149	1537	769
Amstelvar-Roman-YTDE-500.ufo	2000	176	88	176	88	166	83	176	88	980	490	980	490	656	328	843	422	1176	588	176	88	292	146	292	146	80	40	226	113	64	32	74	37	124	62	124	62	111	56	130	65	1534	767	-1000	-500	1520	760	1520	760	1022	511	1520	760	-998	-499	1537	769
Amstelvar-Roman-opsz8-wght100-wdth50.ufo	2000	110	55	110	55	109	55	112	56	694	347	694	347	491	246	616	308	865	433	110	55	222	111	222	111	69	35	178	89	54	27	66	33	100	50	100	50	108	54	113	57	1514	757	-480	-240	1520	760	1520	760	1069	535	1520	760	-510	-255	1509	755
Amstelvar-Roman-opsz8-wght100-wdth100.ufo	2000	120	60	120	60	117	59	118	59	1064	532	1064	532	739	370	874	437	1155	578	120	60	318	159	318	159	85	43	256	128	68	34	78	39	104	52	104	52	108	54	118	59	1509	755	-480	-240	1520	760	1520	760	1072	536	1520	760	-510	-255	1516	758
Amstelvar-Roman-opsz8-wght100-wdth125.ufo	2000	124	62	124	62	124	62	115	58	1450	725	1450	725	1128	564	1222	611	1550	775	124	62	406	203	406	203	101	51	350	175	94	47	98	49	100	50	100	50	108	54	116	58	1509	755	-480	-240	1520	760	1520	760	1081	541	1520	760	-510	-255	1497	749
Amstelvar-Roman-opsz8-wght900-wdth50.ufo	2000	531	266	531	266	511	256	517	259	684	342	684	342	626	313	663	332	1289	645	531	266	129	65	129	65	49	25	122	61	38	19	45	23	200	100	200	100	200	100	211	106	1534	767	-480	-240	1527	764	1527	764	1123	562	1525	763	-496	-248	1515	758
Amstelvar-Roman-opsz8-wght900-wdth100.ufo	2000	541	271	541	271	522	261	533	267	1045	523	1045	523	868	434	955	478	1613	807	541	271	222	111	222	111	65	33	183	92	52	26	60	30	204	102	204	102	200	100	205	103	1534	767	-480	-240	1527	764	1527	764	1126	563	1525	763	-496	-248	1534	767
Amstelvar-Roman-opsz8-wght900-wdth125.ufo	2000	545	273	545	273	527	264	531	266	1431	716	1431	716	1255	628	1178	589	1897	949	545	273	310	155	310	155	81	41	290	145	74	37	79	40	204	102	204	102	212	106	201	101	1534	767	-480	-240	1527	764	1527	764	1135	568	1525	763	-496	-248	1529	765
Amstelvar-Roman-opsz144-wght100.ufo	2000	63	32	63	32	56	28	59	30	904	452	904	452	644	322	904	452	1100	550	63	32	254	127	254	127	70	35	211	106	52	26	64	32	21	11	21	11	24	12	18	9	1490	745	-460	-230	1519	760	1519	760	942	471	1520	760	-482	-241	1499	750
Amstelvar-Roman-opsz144-wght100-wdth50.ufo	2000	53	27	53	27	48	24	43	22	534	267	534	267	401	201	422	211	574	287	53	27	158	79	158	79	54	27	131	66	38	19	50	25	22	11	22	11	24	12	14	7	1494	747	-460	-230	1519	760	1519	760	939	470	1520	760	-482	-241	1510	755
Amstelvar-Roman-opsz144-wght100-wdth125.ufo	2000	59	30	59	30	56	28	57	29	1290	645	1290	645	1042	521	1212	606	1446	723	59	30	346	173	346	173	86	43	306	153	78	39	82	41	27	14	27	14	24	12	18	9	1490	745	-460	-230	1519	760	1519	760	951	476	1520	760	-482	-241	1480	740
Amstelvar-Roman-opsz144-wght400-wdth125.ufo	2000	167	84	167	84	154	77	158	79	1250	625	1250	625	991	496	1061	531	1375	688	167	84	316	158	316	158	81	41	275	138	74	37	74	37	29	15	29	15	43	22	31	16	1511	756	-460	-230	1519	760	1519	760	951	476	1520	760	-490	-245	1493	747
Amstelvar-Roman-opsz144-wght900-wdth50.ufo	2000	474	237	474	237	451	226	458	229	623	312	623	312	546	273	523	262	1018	509	474	237	72	36	72	36	34	17	60	30	22	11	30	15	60	30	60	30	84	42	48	24	1513	757	-460	-230	1518	759	1518	759	993	497	1525	763	-468	-234	1526	763
Amstelvar-Roman-opsz144-wght900-wdth100.ufo	2000	484	242	484	242	462	231	474	237	885	443	885	443	773	387	706	353	1284	642	484	242	158	79	158	79	50	25	138	69	36	18	41	21	65	33	65	33	84	42	52	26	1511	756	-460	-230	1526	763	1526	763	996	498	1525	763	-468	-234	1507	754
Amstelvar-Roman-opsz144-wght900-wdth125.ufo	2000	488	244	488	244	467	234	472	236	1271	636	1271	636	1159	580	1078	539	1688	844	488	244	246	123	246	123	66	33	232	116	62	31	60	30	63	32	63	32	84	42	52	26	1511	756	-460	-230	1526	763	1526	763	1005	503	1525	763	-468	-234	1488	744
"""
measurements = []
for line in measurements_str.splitlines():
    fields = line.split('\t')
    measurements.append(fields)
del line, fields


#pins = {axis:axes[axis][1] for axis in derived_axes}
#print("Loading Amstelvar full font")
#font = ttLib.TTFont('Amstelvar-Roman[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,wdth,wght,opsz].ttf')
#print("Pinning derived axes")
#instantiateVariableFont(font, pins)

# ~/fonttools/fonttools varLib.instancer Amstelvar-Roman[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,wdth,wght,opsz].ttf wdth=100 wght=400 opsz=14

print("Loading Amstelvar pinned font")
font = ttLib.TTFont('Amstelvar-Roman[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,wdth,wght,opsz]-partial.ttf')


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
derived_axes = [ax for ax in axes.keys() if ax not in source_axes]

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

# Update our axis order
axes_new = {}
assert set(axis.axisTag for axis in fvar.axes) == set(axes.keys())
for axis in fvar.axes:
    axes_new[axis.axisTag] = axes[axis.axisTag]
axes = axes_new
source_axes = [ax for ax in fvar_axes if ax not in derived_axes]
del axis, axes_new


import re
source_locations = {}
derived_locations = {}
for fields in measurements:
    key = fields[0]

    # derived location
    values = re.findall(r'-([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])(-?[0-9]+)', key)
    location = derived_locations[key] = {}
    for tag, value in values:
        location[tag] = int(value)

    # source location
    upem = int(fields[1])
    assert upem == 2000
    location = {}
    for axis in source_axes:
        try:
            i = measurements_order.index(axis)
        except ValueError:
            pass
            #continue
        assert i >= 2
        value = int(fields[i]) * 1000 / upem
        location[axis] = value
    source_locations[key] = location
del location, key, values, tag, value


# Axes min/default/max seem to be wrong. Update manually.
# First measurement is for base master:
orig_axes = axes.copy()
name, default_loc = next(iter(source_locations.items()))
assert name.find('Regular')
min_loc = {axis:min(m[axis] for m in source_locations.values()) for axis in source_axes}
max_loc = {axis:max(m[axis] for m in source_locations.values()) for axis in source_axes}
for axis in source_axes:
    axes[axis] = (min_loc[axis], default_loc[axis], max_loc[axis])
del name, axis, default_loc, min_loc, max_loc


print("Modeling avar2")
from fontTools.varLib import models
from fontTools.varLib import varStore
from fontTools.ttLib.tables import otTables


source_locations_normalized = {key:models.normalizeLocation(loc, axes) for key,loc in source_locations.items()}
derived_locations_normalized = {key:models.normalizeLocation(loc, orig_axes) for key,loc in derived_locations.items()}

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

varIdxMap = otTables.DeltaSetIndexMap()
varIdxMap.mapping = []
for axis in fvar.axes:
    tag = axis.axisTag
    varIdxMap.mapping.append(varIdxes[tag])

print("Update various VarStores")
stores = []
if 'GDEF' in font:
    stores.append(font['GDEF'].table.VarStore)
if 'HVAR' in font:
    stores.append(font['HVAR'].table.VarStore)
if 'MVAR' in font:
    stores.append(font['MVAR'].table.VarStore)
nullRegion = otTables.VarRegionAxis()
nullRegion.StartCoord = -1
nullRegion.PeakCoord = 0
nullRegion.EndCoord = 1
for store in stores:
    store.VarRegionList.RegionAxisCount = len(fvar_axes)
    for region in store.VarRegionList.Region:
        while len(region.VarRegionAxis) < len(fvar_axes):
            region.VarRegionAxis.append(nullRegion)

print("Generating avar2")
avar_t = font['avar'] = ttLib.getTableClass('avar')()
avar_t.majorVersion = 2
avar_t.segments = {}
for axis in fvar_axes:
    avar_t.segments[axis] = {}
avar = avar_t.table = otTables.avar()
segMap = otTables.AxisSegmentMap()
segMap.AxisValueMap = []
avar.AxisSegmentMap = [segMap] * len(fvar_axes)
avar.VarIdxMap = varIdxMap
avar.VarStore = store

print("Saving Amstelvar-avar2.ttf")
font.save('Amstelvar-avar2.ttf')

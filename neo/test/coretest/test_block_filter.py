from neo.core import (Segment, Block, Unit, SpikeTrain,
                      RecordingChannelGroup, AnalogSignal)
import quantities as pq
blk = Block()
rcg = RecordingChannelGroup(name='group0')
blk.recordingchannelgroups = [rcg]
for ind in range(5):
    unit = Unit(name='Unit #%s' % ind, channel_indexes=ind)
    rcg.units.append(unit)
    # print "Channel index of unit", unit.channel_indexes

for ind in range(3):
    seg = Segment(name='Simulation #%s' % ind)
    blk.segments.append(seg)
    for unit in rcg.units:
        train = SpikeTrain([1, 2, 3], units='ms', t_start=0.,
                           t_stop=10)
        train.unit = unit
        unit.spiketrains.append(train)
        seg.spiketrains.append(train)
        ana = AnalogSignal(signal=[.01, 3.3, 9.3], units='uV',
                           sampling_rate=1*pq.Hz, channel_index=0)
        # print ".......", ana.channel_index
        seg.analogsignals.append(ana)

print "Block ", blk
print
print "Block filter ", blk.filter(objects="test")
print
print "Block segments Analogsignals ", blk.segments[0].analogsignals[0]
print
print "Block segments annotate a=5 "
blk.segments[0].analogsignals[0].annotate(a=5)
print "Block segments annotate b=6"
blk.segments[1].analogsignals[0].annotate(b=6)
print "Block segments annotate c=7"
blk.segments[1].analogsignals[2].annotate(c=7)
print "Block segments annotate st=8"
blk.segments[2].spiketrains[0].annotate(st=8)

print
print "Block segments annotate st21 unit_id=0"
blk.segments[2].spiketrains[1].annotate(unit_id=0)
print "Block segments annotate st21 electrode_id=7"
blk.segments[2].spiketrains[1].annotate(electrode_id=7)
print "Block segments annotate st22 unit_id=1 "
blk.segments[2].spiketrains[2].annotate(unit_id=1)
print "Block segments annotate st22 electrode_id=7 "
blk.segments[2].spiketrains[2].annotate(electrode_id=7)

# print "Block filter name=Simulation ", blk.filter(name="Simulation #2", container=True)
# print
# print "Block filter a=5 and objects=['AnalogSignal'] ", blk.filter(a=5, \
#                                                                 objects=['AnalogSignal'])
# print
# print "Block filter a=5 and objects=AnalogSignal ", blk.filter(a=5, \
#                                                                objects=AnalogSignal)
# print
# print "Block filter a=5 and objects='ANALOGSiGnal' ", blk.filter(a=5, \
#                                                                  objects='ANALOgSiGnal')
# print
# print "Block filter a=5 and objects='AnalogSignal' ", blk.filter(a=5, \
#                                                                  objects='AnalogSignal')
# print
# print "Block filter a=5 and objects='analogsignal' ", blk.filter(a=5, \
#                                                                  objects='analogsignal')
# print
# print "Unidentified object ", blk.filter(a=5, objects='asdasfasfa')
# print
# print "Block size = ", blk.size
# print
# print "Block filter st=8 and objects='SpikeTrain' ", blk.filter(st=8,
#                                                                 objects='SpikeTrain')
# print
# print "targdict is None and objects='AnalogSignal' ", blk.filter(objects='AnalogSIGnal')
# print
# print "targdict={} and objects='AnalogSignal' ", blk.filter(targdict={}, objects='ANALOGSignal')
# print
# print "targdict={} and objects=AnalogSignal ", blk.filter(targdict={}, objects=AnalogSignal)
# print
# print "targdict={} and objects=['SPikETRAin'] ", blk.filter(targdict={}, objects=["SPikETRAin"])
# print
# print "targdict={} and objects=['SPikETRAin', 'AnalogSIGNAl', 'BLOCK'] ", blk.filter(targdict={}, objects=["SPikETRAin", "AnaLOGSIgnal", "BLOCK"])
# print
# print "targdict={'a':5, 'b':6, 'c':7 } and objects='AnalogSignal' ", blk.filter(targdict={'a': 5, 'b':6, 'c': 7}, objects='AnalogSignal')
# print
# print "targdict={'st':8} and objects='SpikeTrain' ", blk.filter(targdict={'st': 8}, objects='SpikeTrain')
# print
# print "targdict={'st':8, 'c':7 } and objects='AnalogSignal' ", blk.filter(targdict={'st': 8, 'c': 7}, objects=['AnalogSignal', 'SpikeTrain'])
print
print "targdict=[{'unit_id':0, 'unit_id':1},{'electrode_id':7}] and objects='SpikeTrain' ", blk.filter(targdict=[{'unit_id': 0, 'unit_id': 1}, {'electrode_id': 7}], objects=SpikeTrain)

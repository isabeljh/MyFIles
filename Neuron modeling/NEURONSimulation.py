from neuron import h, rxd
from neuron.units import ms,mV,um
import matplotlib.pyplot as plt

#initial numbers
Rm = 40000
Ra = 200
a1 = 10
a2 = 20

axon1 = h.Section(name = 'axon')

axon1.L = 5000 * um
axon1.nseg = 1000
axon1.diam = a1 * um
axon1.Ra = Ra #ohm*cm
axon1.insert('hh')


axon2 = h.Section(name = 'axon')
axon2.L = 5000 *um
axon2.nseg = 1000
axon2.diam = a2 * um
axon2.Ra = Ra #ohm*cm
axon2.insert('hh')

#%%
#calculating length constant
lambda1 = ((a1*0.0001*Rm)/(2*Ra))**(0.5)
lambda2 = ((a2*0.0001*Rm)/(2*Ra))**(0.5)

#%%

iclamp1 = h.IClamp(axon1(0))
iclamp1.dur = .1 * ms
iclamp1.amp = 50 #mA
iclamp1.delay = 1 * ms

iclamp2 = h.IClamp(axon2(0))
iclamp2.dur = .1 * ms
iclamp2.amp = 32 #mA
iclamp2.delay = 4 * ms


v1start = h.Vector().record(axon1(0)._ref_v)
t = h.Vector().record(h._ref_t)

v1halfway = h.Vector().record(axon1(1)._ref_v)

v2start = h.Vector().record(axon2(0)._ref_v)
v2halfway = h.Vector().record(axon2(0.5)._ref_v)

h.load_file('stdrun.hoc')
h.finitialize(-65  *  mV)
h.continuerun(40*ms)
#print(soma1.psection())


plt.figure()
#line1, = plt.plot(t,v1start)
#line2, = plt.plot(t,v1halfway)

#plt.figure()
#line3, = plt.plot(t,v2start)
line4, = plt.plot(t,v2halfway)

plt.title('stim of 50mA')
plt.xlabel('time (ms)')
plt.ylabel('voltage (mV)')
#plt.legend((line1, line2, line3, line4),('Axon1 start','Axon1 end','Axon2 start', 'Axon2 end'))
plt.show()
#%%
from neuron import h, rxd
from neuron.units import ms,mV,um
import matplotlib.pyplot as plt
import numpy as np

sf = 0.5 #scale factor
soma = h.Section(name = 'soma')
soma.L = 24*sf * um
soma.diam = 21*sf *um
soma.nseg = 100
soma.insert('hh')
soma.insert('pas')
soma.insert('extracellular')

dendrite = h.Section(name = 'dendrite')
dendrite.L = 50 *sf *um
dendrite.diam = 12 *sf*um
dendrite.nseg = 222
dendrite.insert('hh')
dendrite.insert('pas')
dendrite.insert('extracellular')

axonnm = h.Section(name = 'axon')
axonnm.L = 16*sf * um
axonnm.diam = 1 *sf* um
axonnm.nseg = 100
axonnm.insert('hh')
for seg in axonnm:
    seg.hh.gnabar = 1.2
    seg.hh.gkbar = 0.36
axonnm.insert('pas')
axonnm.insert('extracellular')


axonm = h.Section(name = 'axon')
axonm.L = 300*sf * um
axonm.diam = 1*sf* um
axonm.nseg = 100
axonm.cm = 0.04
axonm.insert('pas')
axonm.insert('extracellular')

axonhillock = h.Section(name = 'axon')
axonhillock.nseg = 9
axonhillock(0.1).diam = 21*sf
axonhillock.L = 16 *sf *um
x = np.linspace(21,1,9)
x = x[::-1]
for j in np.arange(0,9):
    axonhillock(1-(j+1)*(1/9)).diam = x[j]
axonhillock.insert('hh')
axonhillock.insert('pas')
axonhillock.insert('extracellular')


soma.connect(dendrite)
axonhillock.connect(soma)
axonnm.connect(axonhillock)
axonm.connect(axonnm)
h.topology

#%%
iclamp = h.IClamp(dendrite(0))
iclamp.dur = .1 * ms
iclamp.amp = 3 #mA
iclamp.delay = 1 * ms

i_soma = h.Vector().record(soma(0.5)._ref_i_membrane)
i_dendrite = h.Vector().record(dendrite(0.5)._ref_i_membrane)
i_axonnm = h.Vector().record(axonnm(0.5)._ref_i_membrane)
i_axonm = h.Vector().record(axonm(0.5)._ref_i_membrane)
tt = h.Vector().record(h._ref_t)
h.load_file('stdrun.hoc')
h.finitialize(-65  *  mV)
h.continuerun(10*ms)

plt.figure()
line1, = plt.plot(tt,i_dendrite)
line2, = plt.plot(tt,i_soma)
line3, = plt.plot(tt,i_axonnm)
line4, = plt.plot(tt,i_axonm)

plt.title('stim of 3mA at 0.5x size')
plt.xlabel('time (ms)')
plt.ylabel('current (mA)')
plt.legend((line1, line2, line3, line4),('Dendrite','Soma','Non-myelinated Axon', 'Myelinated Axon'))
plt.show()




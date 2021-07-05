# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:52:17 2020

@author: 91948
"""

from opentrons import simulate
metadata = {'apiLevel': '2.8'}
protocol = simulate.get_protocol_api('2.8')

#Labware
plate = protocol.load_labware('costar96flatbottomtransparent_96_wellplate_200ul', 1)
tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
reservoir = protocol.load_labware('brooksreservoirplate_12_wellplate_21000ul', 3)
#pipettes
p300 = protocol.load_instrument('p300_multi', 'left', tip_racks=[tiprack_1])
protocol.max_speeds['Z'] = 10
#commands

#reservoir A1 contains PBS
#reservoir A2 contains dye

#distributing pbs
p300.distribute(100, reservoir.wells_by_name()['A1'], plate.rows_by_name()['A'][1:])

#distributing dye
for i in range(2):
    p300.transfer(100,reservoir['A2'], plate['A'+str(i+1)], touch_tip=True, blow_out=True, blowout_location='destination well', new_tip='always')

#serial dilution
for i in range(9):
    p300.transfer(100,plate['A'+str(i+2)], plate['A'+str(i+3)], touch_tip=True, blow_out=True, blowout_location='destination well', new_tip='always')

for line in protocol.commands(): 
        print(line)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:49:56 2019

@author: colemanbeggs
"""

import statistics as stats
import math 

# Rubber Side
FricRubber = [0.546, 0.543, 0.549, 0.544, 0.548, 0.540, 0.551, 0.542, 0.551]
avgFricRubber = 0
for i in FricRubber:
    avgFricRubber += i
avgFricRubber /= len(FricRubber)
stdFricRubber = stats.stdev(FricRubber)
z = 1.96

# Wood Side
FricWood = [0.279, 0.275, 0.283, 0.270, 0.288, 0.274, 0.284, 0.277, 0.281]
avgFricWood = 0
for n in FricWood:
    avgFricWood += n
avgFricWood /= len(FricWood)
stdFricWood = stats.stdev(FricWood)
z = 1.96

Confidence = avgFricRubber - stdFricRubber/math.sqrt(len(FricRubber))
Confidence1 = avgFricRubber + stdFricRubber/math.sqrt(len(FricRubber))

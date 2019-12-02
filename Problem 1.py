# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:48:48 2019

@author: Prancis Fayat
"""
import pandas as pd

math = {"Student": ["Ice Bear", "Panda", "Grizzly"], "Math": [80,95,79]}
electronics = {"Student": ["Ice Bear", "Panda", "Grizzly"], "Electronics": [85,81,83]}
geas = {"Student": ["Ice Bear", "Panda", "Grizzly"], "GEAS": [90,79,93]}
esat = {"Student": ["Ice Bear", "Panda", "Grizzly"], "ESAT": [93,89,88]}

mathdf = pd.DataFrame(math, columns = ["Student", "Math"])
elecsdf = pd.DataFrame(electronics, columns = ["Student","Electronics"])
geasdf = pd.DataFrame(geas, columns = ["Student","GEAS"])
esatdf = pd.DataFrame(esat, columns = ["Student","ESAT"])

bear = pd.merge(pd.merge(mathdf,elecsdf, on = "Student"),pd.merge(geasdf, esatdf, on = "Student") , on = "Student")

bearslong = pd.melt(bear, id_vars = ["Student"], var_name = "Subject", value_name = "Grades")
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:46:18 2019

@author: Prancis Fayat
"""
import pandas as pd
boxes = {"Box": ["Box1", "Box1","Box1","Box2","Box2","Box2"], 
         "Dimension": ["Length","Width","Height","Length","Width","Height"],
         "Value": [6,4,2,5,3,4]}
boxesdf = pd.DataFrame(boxes, columns = ["Box", "Dimension", "Value"])

boxestidy = boxesdf.pivot_table(index = "Box", columns = "Dimension", values = "Value")
boxestidy['Volume'] = boxestidy.Length * boxestidy.Width * boxestidy.Height


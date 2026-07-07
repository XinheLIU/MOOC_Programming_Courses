# -*- coding: utf-8 -*-
"""
create DataFrame object

@author: Dazhuang
"""
import pandas as pd
music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]
music_table = pd.DataFrame(music_data)
music_table.index = range(1, 5)                          
music_table.columns = ['singer', 'song_name']
print(music_table)
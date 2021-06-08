import numpy as np
from geneticalgorithm import geneticalgorithm as ga
def fire(type,number_of_stories):
    fire_time=0
    #type1:omumy
    #type2:khososy
    #type3:khososy more than 300
    #type 4:spetial
    width_min_c=24
    height_min_c=24
    width_min_b=20
    height_min_b=20
    if type==1:
        fire_time=150
    if type==2 and 2<number_of_stories<5:
        fire_time=60
        width_min_c=20
        height_min_c=20
        width_min_b=20
        height_min_b=20

    if type==2 and 6<number_of_stories<10:
        fire_time=90
        width_min_c=24
        height_min_c=24
        width_min_b=20
        height_min_b=20
    if type==2 and 11<number_of_stories<20:
        fire_time=120
        width_min_c=30
        height_min_c=30
        width_min_b=25
        height_min_b=25
    if type==3 :
        fire_time=150
        width_min_c=35
        height_min_c=35
        width_min_b=25
        height_min_b=25
    if type==4:
        fire_time=240
        width_min_c=45
        height_min_c=45
        width_min_b=35
        height_min_b=35
    minimum_fire={
        "width_min_c":width_min_c,
        "height_min_c":height_min_c,
        "width_min_b": width_min_b,
        "height_min_b":height_min_b


    }
    return minimum_fire



def min_sheklpaziri(type):
    width_min_c=25
    height_min_c=25
    width_min_b=25
    height_min_b=25
    #type1:normal
    #type2:spetcial
    #type3:low
    if type==1:
        width_min_c=25
        height_min_c=25
        width_min_b=25
        height_min_b=25
    if type==2:
        width_min_c=30
        height_min_c=30
        width_min_b=25
        height_min_b=25
    result={
        "width_min_c":width_min_c,
        "height_min_c":height_min_c,
        "width_min_b": width_min_b,
        "height_min_b":height_min_b
    }
    return result








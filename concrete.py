import comtypes.client as cm
from base import *
from LowerBand import fire,min_sheklpaziri
import math
import pandas as pd

def get_num_story():
    return story.GetStories()
#0:number of stroies
#1: name of stories
#elevation of stories
def get_all_frames():

    return FrameObj.GetLabelNameList()

def get_columns():
    columns=[[],[],[]]
    lentgh=FrameObj.GetLabelNameList()[0]
    labels=FrameObj.GetLabelNameList()[2]
    uniq_name=FrameObj.GetLabelNameList()[1]
    stroies=FrameObj.GetLabelNameList()[3]

    for i in range(lentgh):
        if labels[i][0]=="C":
            columns[0].append(uniq_name[i])
            columns[1].append(labels[i])
            columns[2].append(stroies[i])
    return columns

def get_beams():
    beams=[[],[],[]]
    lentgh=FrameObj.GetLabelNameList()[0]
    labels=FrameObj.GetLabelNameList()[2]
    uniq_name=FrameObj.GetLabelNameList()[1]
    stroies=FrameObj.GetLabelNameList()[3]
    for i in range(lentgh):
        if labels[i][0]=="B":
            beams[0].append(uniq_name[i])
            beams[1].append(labels[i])
            beams[2].append(stroies[i])
    return beams

def set_unit():
    #Kn:4
    #kgf:5
    #N:3
    SapModel.SetPresentUnits_2(5, 5,2)

set_unit()


def get_section_prop():
    uniq_names=get_all_frames()[1]
    sections=[]
    for i in uniq_names:
        sections.append(FrameObj.GetSection(i))
    return sections

def get_section_dim():
    sections=get_section_prop()
    heights_width={}
    widths=[]
    heights=[]
    for s in sections:
        se=s[0]
        dimentios=PropFrame.GetRectangle(se)
        widths.append(int(dimentios[2]))
        heights.append(int(dimentios[3]))
    heights_width={
        "widths":widths,
        "heights":heights,
        "heights_norepeat":list(set(heights)),
        "width_norepeat":list(set(widths))

    }
    return heights_width



#print(pp.pprint(get_section_dim()["width_norepeat"]))

def upper_band():

    widths_max=max(get_section_dim()["width_norepeat"])
    heights_max=max(get_section_dim()["heights_norepeat"])
    result={
        "widths_max":math.ceil(widths_max*1.15/5)*5,
        "heights_max":math.ceil(heights_max*1.15/5)*5
    }
    return result

def creat_upper_lower():
    result={
        "min_beam_width":max(fire(type=2,number_of_stories=get_num_story()[0])['width_min_b'],
                             min_sheklpaziri(type=1)['width_min_b']),
        "min_beam_height":max(fire(type=2,number_of_stories=get_num_story()[0])['height_min_b'],
                              min_sheklpaziri(type=1)['height_min_b']),
        "min_column_width":max(fire(type=2,number_of_stories=get_num_story()[0])['width_min_c'],
                               min_sheklpaziri(type=1)['width_min_c']),
        "min_column_height":max(fire(type=2,number_of_stories=get_num_story()[0])['height_min_c'],
                                min_sheklpaziri(type=1)['height_min_c']),
        "max_beam_width":65,
        "max_beam_height":65,
        "max_column_width":upper_band()['widths_max'],
        "max_column_height":upper_band()['heights_max'],
    }
    return result


def creat_first_table():
    cars = {'Uniq_name':get_all_frames()[1],
            'label': get_all_frames()[2],
            'story':get_all_frames()[3],
            "section":[x[0] for x in get_section_prop()],
            "width":get_section_dim()["widths"],
            "height":get_section_dim()["heights"],
            "length":get_lengh(),

            }

    df = pd.DataFrame(cars, columns = ['Uniq_name','label',"story",'section','width',"height","length"])
    df["Area"]=df['width']*df["height"]
    df["volume"]=df["Area"]*df["length"]
    return df

def get_poits():
    frame_uniq_names=get_all_frames()[1]
    all_points=[]
    for frame in frame_uniq_names:
        all_points.append(FrameObj.GetPoints(frame))
    return all_points

print(get_poits())
def get_lengh():
    points=get_poits()
    re=[]
    print(PointObj.GetCoordCartesian(points[0][0])[0:3])
    print(PointObj.GetCoordCartesian(points[0][1])[0:3])
    for x in points:
        x1,y1,z1=PointObj.GetCoordCartesian(x[0])[0:3]
        x2,y2,z2=PointObj.GetCoordCartesian(x[1])[0:3]
        re.append(((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5)
    return re

print(creat_first_table())






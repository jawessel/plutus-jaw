# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:24:58 2023

@author: jaw22
"""

# Templates for making tidy CSV's out of GCAM XML's

from lxml import etree

###############################################################################

##### takes institutional factors XML and flattens for CSV #####

# with open(r'inst_factors_mult_LAC.xml', 'r') as xml:
#     text = xml.read()
# tree = etree.fromstring(text)[0]
# row = ['','','','','','']
# for item in tree.iter('region','supplysector','pass-through-sector','subsector',\
#                       'stub-technology','intermittent-technology','period','fixed-charge-rate'):
#     if item.tag == 'region':
#         row[0] = item.attrib['name']
#     elif item.tag == 'supplysector':
#         row[1] = item.attrib['name']
#     elif item.tag == 'pass-through-sector':
#         row[1] = item.attrib['name']
#     elif item.tag == 'subsector':
#         row[2] = item.attrib['name']
#     elif item.tag == 'stub-technology':
#         row[3] = item.attrib['name']
#     elif item.tag == 'intermittent-technology':
#         row[3] = item.attrib['name']
#     elif item.tag == 'period':
#         row[4] = item.attrib['year']
#     elif item.tag == 'fixed-charge-rate':
#         row[5] = item.text

#         line = ','.join(row)

#         with open(r'inst_FCR.csv', 'a') as csv:
#             csv.write(line + '\n')


##### takes wind_adv XML and flattens for CSV #####

# with open(r'wind_adv.xml', 'rb') as xml:
#     text = xml.read()
# tree = etree.fromstring(text)[0][0][0]
# row = ['','','','','','']
# for item in tree.iter('location-info','technology','intermittent-technology','period','capital-overnight'):
#     if item.tag == 'location-info':
#         row[0] = item.attrib['sector-name']
#         row[1] = item.attrib['subsector-name']
#     elif item.tag == 'technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'intermittent-technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'period':
#         row[3] = item.attrib['year']
#     elif item.tag == 'capital-overnight':
#         row[4] = item.text

#         line = ','.join(row)

#         with open(r'wind_adv_cap.csv', 'a') as csv:
#             csv.write(line + '\n')

##### takes wind_low XML and flattens for CSV #####

# with open(r'wind_low.xml', 'rb') as xml:
#     text = xml.read()
# tree = etree.fromstring(text)[0][0][0]
# row = ['','','','','','']
# for item in tree.iter('location-info','technology','intermittent-technology','period','capital-overnight'):
#     if item.tag == 'location-info':
#         row[0] = item.attrib['sector-name']
#         row[1] = item.attrib['subsector-name']
#     elif item.tag == 'technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'intermittent-technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'period':
#         row[3] = item.attrib['year']
#     elif item.tag == 'capital-overnight':
#         row[4] = item.text

#         line = ','.join(row)

#         with open(r'wind_low_cap.csv', 'a') as csv:
#             csv.write(line + '\n')

##### takes solar_adv XML and flattens for CSV #####

# with open(r'solar_adv.xml', 'rb') as xml:
#     text = xml.read()
# tree = etree.fromstring(text)[0][0]
# row = ['','','','','','']
# for item in tree.iter('location-info','technology','intermittent-technology','period','capital-overnight'):
#     if item.tag == 'location-info':
#         row[0] = item.attrib['sector-name']
#         row[1] = item.attrib['subsector-name']
#     elif item.tag == 'technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'intermittent-technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'period':
#         row[3] = item.attrib['year']
#     elif item.tag == 'capital-overnight':
#         row[4] = item.text

#         line = ','.join(row)

#         with open(r'solar_adv_cap.csv', 'a') as csv:
#             csv.write(line + '\n')

##### takes solar_low XML and flattens for CSV #####

# with open(r'solar_low.xml', 'rb') as xml:
#     text = xml.read()
# tree = etree.fromstring(text)[0][0]
# row = ['','','','','','']
# for item in tree.iter('location-info','technology','intermittent-technology','period','capital-overnight'):
#     if item.tag == 'location-info':
#         row[0] = item.attrib['sector-name']
#         row[1] = item.attrib['subsector-name']
#     elif item.tag == 'technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'intermittent-technology':
#         row[2] = item.attrib['name']
#     elif item.tag == 'period':
#         row[3] = item.attrib['year']
#     elif item.tag == 'capital-overnight':
#         row[4] = item.text

#         line = ','.join(row)

#         with open(r'solar_low_cap.csv', 'a') as csv:
#             csv.write(line + '\n')

###############################################################################














import xml.etree.ElementTree as ET

tree = ET.parse("dane.xml")
root = tree.getroot()
title = 'Reservoir Dogs'
root.find("./genre/decade/movie[@title='"+title+"']/year").text = '2023'
tree.write("output.xml")
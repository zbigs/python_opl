import xml.etree.ElementTree as ET

tree = ET.parse("dane.xml")
root = tree.getroot()
root.find("./genre/decade/movie[@title='Reservoir Dogs']/year").text = '2023'
tree.write("output.xml")
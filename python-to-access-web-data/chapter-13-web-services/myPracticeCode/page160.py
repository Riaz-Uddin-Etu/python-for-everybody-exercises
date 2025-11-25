# Parsing XML using ElementTree parser
import xml.etree.ElementTree as ET

data = ''' 
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person> '''

tree = ET.fromstring(data)

print('NAME: ', tree.find('name').text)
print('ATTR: ', tree.find('email').get('hide'))

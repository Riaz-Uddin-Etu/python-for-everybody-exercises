import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

# to get xml from string create a subtree
tree = ET.fromstring(data)

lst = tree.findall('users/user')
print(len(lst)) # return 2 

lst2 = tree.findall('stuff/users')
print(len(lst2)) # return 0 | So don't use top level element


for element in lst:
    print("ID: ", element.find('id').text)
    print("NAME: ", element.find('name').text)
    print("ATTR: ", element.get('x'))



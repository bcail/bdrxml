from eulxml import xmlmap
from eulxml.xmlmap import XmlObject
from eulxml.xmlmap import StringField as SF

MODS_NAMESPACE = 'http://www.loc.gov/mods/v3'
MODS_SCHEMA = 'http://www.loc.gov/standards/mods/v3/mods-3-3.xsd'

class Collection(XmlObject):
    ROOT_NAME = 'relatedItem'
    name = SF('mods:titleInfo/mods:title')
    id = SF('mods:identifier[@type="COLID"]')
    
class PersonalName(XmlObject):
    ROOT_NAME = 'name'
    namePart = SF('mods:namePart')
    years = SF('mods:namePart[@type="date"]')
    role = SF('mods:role/mods:roleTerm')

class CorporateName(XmlObject):
    ROOT_NAME = 'name'
    namePart = SF('mods:namePart')
    #years = SF('mods:namePart[@type="date"]')
    role = SF('mods:role/mods:roleTerm')

class Subject(XmlObject):
    ROOT_NS = MODS_NAMESPACE
    ROOT_NAME = 'subject'
    topic = SF('mods:topic')

class Mods(XmlObject):
    """Map mods fields."""
    ROOT_NAME = 'mods'
    ROOT_NAMESPACES = {
                   'mods': MODS_NAMESPACE,
                   'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                   }
    schema_location = xmlmap.StringField('@xsi:schemaLocation')
    id = SF('@ID')
    title = SF('mods:titleInfo/mods:title')
    publisher = SF('mods:originInfo/mods:publisher')
    language_code = xmlmap.StringField('mods:language/mods:languageTerm[@type="code"]')
    abstract = SF('mods:abstract')
    extent = SF('mods:physicalDescription/mods:extent')
    collection = xmlmap.NodeField('mods:relatedItem[@displayLabel="Collection"]', Collection)
    genre = SF('mods:genre')
    personal_name = xmlmap.NodeListField('mods:name[@type="personal"]', PersonalName)
    corporate_name = xmlmap.NodeListField('mods:name[@type="corporate"]', CorporateName)
    created = SF('mods:originInfo/mods:dateCreated')
    subject = xmlmap.NodeListField('mods:subject[@type="local"]', Subject)
    

def make_mods():
    """
    Helper that sets the XSD and returns Mods object.
    """
    m = Mods()
    m.schema_location = MODS_SCHEMA
    return m
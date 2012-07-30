import os
import unittest
from lxml import etree
from eulxml.xmlmap  import load_xmlobject_from_string, load_xmlobject_from_file
from bdrxml.mets import BDRMets, make_mets
from bdrxml.mods import Mods

BASE = os.path.dirname(os.path.abspath(__file__))

class MetsReadWrite(unittest.TestCase):
    def setUp(self):
        #basic fox
        self.mets = load_xmlobject_from_file(os.path.join(BASE, 'data/cdi_mets.xml'),
                                             BDRMets)
        
    def test_read(self):
        #print self.mets.serialize(pretty=True)
        self.assertEqual(self.mets.rights.holder.name, "Brown University")
        self.assertEqual(self.mets.mods.title, "Camp Grant Massacre")
        
    def test_write(self):
        mets = make_mets()
        mods = load_xmlobject_from_file(os.path.join(BASE, 'data/cdi.mods'),
                                        Mods)
        mets.mods = mods
        self.assertEqual(mets.mods.title, "Guerrilla")
        mets.create_rights()
        mets.rights.create_holder()
        mets.rights.holder.name = "BUL"
        self.assertEqual(mets.rights.holder.name, "BUL")
        

def suite():
    suite = unittest.makeSuite(MetsReadWrite, 'test')
    return suite

if __name__ == '__main__':
    unittest.main()
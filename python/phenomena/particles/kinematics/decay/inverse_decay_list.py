
class InverseDecayList(Object):

    def __init__(self,p1,p2):

        import xml.etree.ElementTree as ET
        import os

        base = os.path.dirname(os.path.abspath(__file__))
        searchpaths = (base + '/ParticleData.xml', 'ParticleData.xml',
                       '../ParticleData.xml',
                       'ParticleDataTool/ParticleData.xml')
        xmlname = None
        for p in searchpaths:
            if os.path.isfile(p):
                xmlname = p
                break
        if xmlname is None:
            raise IOError('ParticleDataTool::_load_xml(): '
                          'XML file not found.')
        root = ET.parse(xmlname).getroot()


        k1 = pythia.pdg_id(p1)
        k2 = pythia.pdg_id(p2)
        ids = [k1,k2]

        combs = []

        tags = [str(ids[0]),str(-ids[1])]
        tagsR = [str(-ids[1]),str(ids[0])]
        tagsbar = [str(-ids[0]), str(ids[1])]
        tagsbarR = [str(ids[1]), str(-ids[0])]
        for parent in root:
            if parent.tag == 'particle':
                for channel in parent:
                    if channel.attrib['products'] == ' '.join(tags[0]) or channel.attrib['products'] == ' '.join(tagsR[0]):
                        combs.append(parent.attrib['name'])
                    if channel.attrib['products'] == ' '.join(tagsbar[0]) or channel.attrib['products'] == ' '.join(tagsbarR[0]):
                        combs.append(parent.attrib['antiName'])

        self._virtual_list = combs

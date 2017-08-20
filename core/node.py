import maya.cmds as cmds
import attribute
reload(attribute)


class Light(object):

    def __init__(self, light_node):
        self.light_node = light_node
        self.__attrs = {attr:attribute.Attribute("{light_shape}.{attr}".format(light_shape=self.light_node, attr=attr)) for attr in cmds.listAttr(self.light_node)}
        self.__enabled = True

    @property
    def name(self):
        return self.light_node

    @property
    def attrs(self):
        return self.__attrs

    @property
    def node_type(self):
        return cmds.objectType(self.light_node)

    @property
    def parent(self):
        return cmds.listRelatives(self.light_node, parent=True)[0]

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enable = value

    def attr(self, attr_name):
        return self.attrs.get(attr_name)

    def has_attr(self, attr_name):
        return True if attr_name in self.attrs.keys() else False

    def attr_value(self, attr_name):
        return self.attr.get(attr_name).value
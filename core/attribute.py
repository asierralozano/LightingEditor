import maya.cmds as cmds

class Attribute(object):

    def __init__(self, node):
        self.node = node
    
    @property
    def full_name(self):
        return self.node

    @property
    def name(self):
        return self.node.split(".")[1]

    @property
    def light(self):
        return self.node.split(".")[0]

    @property
    def type(self):
        return cmds.getAttr(self.full_name, type=True)

    @property
    def value(self):
        return cmds.getAttr(self.full_name)

    # @value.setter
    # def value(self, value2set):
    #     cmds.setAttr(self.full_name, value2set, type=self.type)

    @property
    def is_locked(self):
        return cmds.getAttr(self.full_name, locked=True)

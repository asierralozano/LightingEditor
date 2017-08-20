from PySide2 import QtCore, QtGui, QtWidgets

class LightWidget(QtCore.QAbstractItemModel):
    def __init__(self, light_obj):
        super(LightWidget, self).__init__()
        self.light_obj = light_obj

    def __default_state(self):
        label_name = QtWidgets.QLabel(self.light_obj.name)
        enabled_cb = QtWidgets.QComboBox()
        enabled_cb.setCheckState(self.light_obj.enabled)
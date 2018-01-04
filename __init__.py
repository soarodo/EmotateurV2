import Ui_test
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
class InterFaceFunctions():
    def __init__(self):
        self.Form=QtWidgets.QWidget()
        self.ui = Ui_test.Ui_Form()
        self.ui.setupUi(self.Form)
        self.img=QtGui.QPixmap(":/imageEmotions/ImageEmotion1.jpg")
        self.videoCapture=cv2.VideoCapture()
        self.checkSimilarityTimer=QtCore.QTimer()
        if self.videoCapture.open(0):
            self.checkSimilarityTimer.timeout.connect(self.updateFrame)
            self.checkSimilarityTimer.start(1000/20)
            self.ui.label.setPixmap(self.img)
        else :
            print("camera configuration failed")
        
    def updateFrame(self):
        ret, srcMat=self.videoCapture.read()
        srcMat=cv2.resize(srcMat, (320, 240), interpolation=cv2.INTER_CUBIC)
        srcMat=cv2.flip(srcMat, 1)
        cv2.cvtColor(srcMat, cv2.COLOR_BGR2RGB,srcMat)
        height, width, bytesPerComponent= srcMat.shape
        bytesPerLine = bytesPerComponent* width
        srcQImage= QtGui.QImage(srcMat.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        srcQPix=QtGui.QPixmap.fromImage(srcQImage)
        self.ui.videoLable.setPixmap(srcQPix)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfaceFun=InterFaceFunctions()
    interfaceFun.Form.show()
    sys.exit(app.exec_())

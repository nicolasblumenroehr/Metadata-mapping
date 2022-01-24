import pydicom
from pyDicomImage import pyDicomImage

class pyDicom:
    
    def __init__(self, dicomFile, seriesName, seriesLoc, imageFormats: list()):
        self.dicomFile=pydicom.dcmread(dicomFile)
        self.seriesName=seriesName
        self.seriesLocation=seriesLoc
        self.imageFormats=imageFormats

    def studyMetadata(self, studyName: str(), studyLocation: str()):
        self.studyName=studyName
        self.studyLocation=studyLocation

    def seriesMetadata(self):  

        self.repetitionTime=self.dicomFile[0x5200, 0x9229][0][0x0018, 0x9112][0][0x0018, 0x0080].value
        self.flipAngle=self.dicomFile[0x5200, 0x9229][0][0x0018, 0x9112][0][0x0018, 0x1314].value
        self.echoTime=self.dicomFile[0x5200, 0x9229][0][0x0018, 0x9114][0][0x0018, 0x9082].value
        self.imageOrientation=self.dicomFile[0x5200, 0x9229][0][0x0020, 0x9116][0][0x0020,0x0037].value
        self.numberOfImages=self.dicomFile[0x0028, 0x0008].value
        self.sliceThickness=self.dicomFile[0x5200, 0x9229][0][0x0028, 0x9110][0][0x0018,0x0050].value
        self.pixelSpacing=self.dicomFile[0x5200, 0x9229][0][0x0028, 0x9110][0][0x0028,0x0030].value
        self.imageArray=[]
        self.perImage=[]
        for i in range(0, self.dicomFile[0x0028, 0x0008].value):
            dicomImage=pyDicomImage(self.dicomFile, i, self.imageFormats[i])
            dicomImage.imageMetadata()
            self.imageArray.append(dicomImage)
            self.perImage.append(dicomImage)

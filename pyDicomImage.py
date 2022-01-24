from pyDicomPixelArray import pyDicomPixelArray
class pyDicomImage:
    def __init__(self, dicomFile, imageNumber, imageFormat):
        self.dicomFile=dicomFile
        self.imageNumber=imageNumber+1
        self.convertedFormat=imageFormat
    def imageMetadata(self):
        self.positionParameters=self.dicomFile[0x5200, 0x9230][self.imageNumber-1][0x0020, 0x9113][0][0x0020, 0x0032].value
        self.pixelsPerRow=len(self.dicomFile.pixel_array[self.imageNumber-1][0])
        self.pixelsPerColumn=len(self.dicomFile.pixel_array[self.imageNumber-1][0])
        minPixelIntensity=[]
        maxPixelIntensity=[]
        self.pixelArray=[]
        
        for i in range(0, len(self.dicomFile.pixel_array[self.imageNumber-1])):
        #for i in range(0, 3):
            dicomPixel=pyDicomPixelArray(self.dicomFile, self.imageNumber-1, i)
            dicomPixel.pixelMetadata()
            self.pixelArray.append(dicomPixel)
            minPixelIntensity.append(dicomPixel.minPixelIntensity)
            maxPixelIntensity.append(dicomPixel.maxPixelIntensity)

        self.minimum=min(minPixelIntensity)
        self.maximum=max(maxPixelIntensity)


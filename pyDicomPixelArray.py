class pyDicomPixelArray:
    def __init__(self, dicomFile, imageNumber, pixelRow):
        self.dicomFile=dicomFile
        self.imageNumber=imageNumber
        self.pixelRow=pixelRow
    def pixelMetadata(self):
        self.pixelIntensity=self.dicomFile.pixel_array[self.imageNumber][self.pixelRow]
        self.maxPixelIntensity=self.dicomFile.pixel_array[self.imageNumber][self.pixelRow].max()
        self.minPixelIntensity=self.dicomFile.pixel_array[self.imageNumber][self.pixelRow].min()

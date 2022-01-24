import json
import os
import glob
from pyDicom import pyDicom
from fillSchema import fillSchema
from readSchema import readSchema

jsonSchema = open("path/to/.json")
draftDir=glob.glob("path/to/*draft.json")
jsonSchema = json.load(jsonSchema)

readSchema=readSchema()
readSchema.schemaValidator(jsonSchema, draftDir)
schema=readSchema.searchObject(jsonSchema)
studyName="DicomTestStudy"
studyLocation="PATH" #directory or link, where the series of a study are deposited

allDicomSeries=[]
for i in os.listdir(studyLocation+studyName):
    f = os.path.join(studyLocation+studyName, i)
    seriesName=i
    seriesLocation=studyLocation+studyName
    imageFormatsList=["formats"] #one per image in a series
    dicomSeries=pyDicom(f,seriesName, seriesLocation, imageFormatsList)
    dicomSeries.seriesMetadata()
    dicomSeries.studyMetadata(studyName, studyLocation)
    allDicomSeries.append(dicomSeries)

print("Schema structure",schema)
fillSchema=fillSchema()
filledSchema=fillSchema.fillObject(schema, list(schema.keys()), allDicomSeries)
print("Mapping finished")
with open('metadata.json', 'w') as f:
    json.dump(filledSchema, f)

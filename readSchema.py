from jsonschema import validate
class readSchema():

    def schemaValidator(self, jsonSchema, draftDir):
        "Validate the schema file is of proper JSON Format, corresponding to the latest draft supported by this application or earlier"
        
        drafts=[]
        for i in draftDir:
            try:
                if validate(instance=jsonSchema, schema=i) == True:
                    drafts.append(True)
                else:
                    drafts.append(False)

                if True in drafts:
                    print("Valid Schema")
                else:
                    print("No valid Schema")
            except:
                pass

    def searchArray(self, property):
        if property["items"]["type"] == "array":
            subProperties=[self.searchArray(property["items"])]
        elif property["items"]["type"] == "object":
            subProperties=self.searchObject(property["items"])
        else:
            if property["items"]["type"]=="integer":
                subProperties="int"
            elif property["items"]["type"]=="string":
                subProperties="str"
            elif property["items"]["type"]=="number":
                subProperties="float"
            elif property["items"]["type"]=="boolean":
                subProperties="bool"
            elif property["items"]["type"]=="null":
                subProperties=None
            else:
                print(TypeError)

        return subProperties

    def searchObject(self, property):
        properties={}
        for i in property["properties"].items():
            if i[1]["type"] == "array":
                subProperties=self.searchArray(i[1])
                properties[i[0]]=[subProperties]
            elif i[1]["type"] == "object":
                subProperties=self.searchObject(i[1])
                properties[i[0]]=subProperties
            else:
                if i[1]["type"]=="integer":
                    properties[i[0]]="int"
                elif i[1]["type"]=="string":
                    properties[i[0]]="str"
                elif i[1]["type"]=="number":
                    properties[i[0]]="float"
                elif i[1]["type"]=="boolean":
                    properties[i[0]]="bool"
                elif i[1]["type"]=="null":
                    properties[i[0]]=None
                else:
                    print(TypeError)
        return properties

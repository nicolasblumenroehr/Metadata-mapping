class fillSchema:

    def fillObject(self, dictionary: dict(), keys: list(), values: list()):
        newDict={}
        for i in keys:
            if (type(dictionary[i])==type(str())):
                try:
                    for x, y in values[0].__dict__.items():
                        if (i==x): 
                            newDict[i]=str(y)
                except(TypeError):
                    for x, y in values.__dict__.items():
                        if (i==x): 
                            newDict[i]=str(y)

            elif type(dictionary[i])==type(dict()):
                newDict[i]=self.fillObject(dictionary[i], list(dictionary[i].keys()), values)

            elif type(dictionary[i])==type(list()):
                newDict[i]=self.fillArray(dictionary, i, dictionary[i], values)
        return newDict

    def fillArray(self, jsonObject, jsonObjectProperty, jsonArray, newArrayContent):

        if type(newArrayContent)!=type(list()):
            for x, y in newArrayContent.__dict__.items():
                if jsonObjectProperty == x:
                    try:
                        newArrayContent=y
                    except:
                        pass
        try:
            jsonArray=jsonArray*len(newArrayContent)
        except Exception as e:
            print(e)
        newList=[]

        for i, j in zip(jsonArray, range(0, len(jsonArray))):
            if type(i)==type(str()):
                if type(newArrayContent[j])==type(object()):
                    for x, y in newArrayContent[j].__dict__.items():
                        if jsonObjectProperty==x: newList.append(str(y))
                else:
                    newList.append(str(newArrayContent[j]))
            elif type(i)==type(dict()):
                try:
                    newList.append(self.fillObject(i, list(i.keys()), newArrayContent[j]))
                except Exception as e:
                    print(e)
                    pass

            elif type(i)==type(list):
                for x, y in newArrayContent[j].__dict__.items():
                    if i == x:
                        newList.append(self.fillArray(jsonObject, jsonObjectProperty, i, y))

        return newList

from custompromptobject import CustomPromptObject

class CustomPromptObjectContainer:

    def __init__(self):
        self.customPromptList = []

    def addCustomPrompt(self, CustomPromptObject):
        self.customPromptList.append(CustomPromptObject)
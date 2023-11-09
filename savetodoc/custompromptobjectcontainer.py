class CustomPromptObjectContainer:
    def __init__(self, docName):
        self.docName = docName
        self.customPromptList = []

    def addCustomPrompt(self, CustomPromptObject):
        self.customPromptList.append(CustomPromptObject)
from custompromptobjectcontainer import CustomPromptObjectContainer
from custompromptobject import CustomPromptObject
from savetodoc import savetodoc

def test():
    # Now using square brackets for a list, not curly braces for a set
    container = CustomPromptObjectContainer()
    container.addCustomPrompt(CustomPromptObject("Prompt 1"))
    container.addCustomPrompt(CustomPromptObject("Prompt 2"))
    savetodoc(container, "testing")

if __name__ == "__main__":
    test()
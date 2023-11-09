from custompromptobjectcontainer import CustomPromptObjectContainer
from custompromptobject import CustomPromptObject
from savetodoc import save_to_pdf

def test():
    # Now using square brackets for a list, not curly braces for a set
    container = CustomPromptObjectContainer("Testing")
    container.addCustomPrompt(CustomPromptObject("Prompt 1: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 200, 500))
    container.addCustomPrompt(CustomPromptObject("Prompt 2", 0, 400))
    container.addCustomPrompt(CustomPromptObject("Prompt 3: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", 0, 300))
    container.addCustomPrompt(CustomPromptObject("Prompt 4: c", 0, 200))

    save_to_pdf("testing.pdf", container)

if __name__ == "__main__":
    test()
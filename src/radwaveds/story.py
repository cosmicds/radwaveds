from cosmicds.phases import Story
from cosmicds.registries import story_registry
from echo import DictCallbackProperty, CallbackProperty


@story_registry(name="radwave")
class radwaveds(Story):
    title = CallbackProperty("Rad Wave")
    # This is an example attribute on the story class. Information stored here
    # will be available in the front-end UI.
    example_attribute = DictCallbackProperty(
        {'some_info': "Data stories are cool!"})

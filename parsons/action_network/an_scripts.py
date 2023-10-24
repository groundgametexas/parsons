from parsons.action_network import ActionNetwork
import prettyprinter

# Set up prettyprinter
prettyprinter.install_extras(include=['dataclasses'])


an = ActionNetwork()
messages = an.get_messages()

# Print the messages using prettyprinter
prettyprinter.pprint(messages)


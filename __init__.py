from mycroft import MycroftSkill, intent_file_handler


class Killroscore(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('killroscore.intent')
    def handle_killroscore(self, message):
        self.speak_dialog('killroscore')


def create_skill():
    return Killroscore()


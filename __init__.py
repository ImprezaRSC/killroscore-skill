from mycroft import MycroftSkill, intent_file_handler
import subprocess

class Killroscore(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('killroscore.intent')
    def handle_killroscore(self, message):
        self.speak_dialog('killroscore')
        s="killall -e roscore"
        subprocess.call([s],shell=True)
        
def create_skill():
    return Killroscore()


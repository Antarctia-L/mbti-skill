from mycroft import MycroftSkill, intent_file_handler


class Mbti(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mbti.intent')
    def handle_mbti(self, message):
        self.speak_dialog('mbti')


def create_skill():
    return Mbti()


# import language_tool_python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
import language_tool_python


# def check_grammar(text):
#     tool = language_tool_python.LanguageTool('en-US')
#     matches = tool.check(text.capitalize())
#     if len(matches) == 0:
#         return True, text
#     corrected_text = language_tool_python.utils.correct(text, matches)
#     return False, corrected_text


class Chatbot:
    def __init__(self):
        self.model = GigaChat(
            credentials="YTM0YjVmNjQtOWIyMy00N2I4LTg0MjgtZDMwZDU4YjhlOTJkOmJlMDYwNTE4LTQ0NjYtNDRlZC04ZTZmLWEyN2E4MGFmOTY3MA==",
            scope="GIGACHAT_API_PERS",
            model="GigaChat",
            verify_ssl_certs=False,
        )

        self.messages = [
            SystemMessage(
                content="""Ты носитель английского который разговаривает с человеком для его практики английского,
                        Тебя зовут Simba, если пользователь начинает говорить на русском ты говоришь ему переходить
                        на английский
                        """
            )
        ]

    def generate_answer(self, answer):
        self.messages.append(HumanMessage(content=answer))
        res = self.model.invoke(self.messages)
        self.messages.append(res)
        return res.content


def check_grammar(text):
    text = text.capitalize()
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return language_tool_python.utils.correct(text, matches), ' '.join(match.message for match in matches)

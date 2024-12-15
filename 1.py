import language_tool_python


def check_grammar_with_languagetool(text):
    text = text.capitalize()
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return language_tool_python.utils.correct(text, matches), ' '.join(match.message for match in matches)


text = "i want be"
print(check_grammar_with_languagetool(text))
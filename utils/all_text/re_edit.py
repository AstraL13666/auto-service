from emoji import emojize, demojize


class Format:
    """
    Форматирование текста:
    "b" - жирный текст
    "i" - курсивный текст
    "u" - подчеркнутый текст
    "s" - зачеркнутый текст и их комбинации
    """

    def __init__(self):
        self.__bold = '<b>{}</b>'
        self.__italic = '<i>{}</i>'
        self.__underline = '<u>{}</u>'
        self.__strike = '<s>{}</s>'

        self.__bold_italic = '<b><i>{}</i></b>'
        self.__bold_under = '<b><u>{}</u></b>'
        self.__bold_strike = '<b><s>{}</s></b>'

        self.__italic_underline = '<i><u>{}</u></i>'
        self.__italic_strike = '<i><s>{}</s></i>'

        self.__bold_italic_under = '<b><i><u>{}</u></i></b>'
        self.__bold_italic_strike = '<b><i><s>{}</s></i></b>'

        self.__data = {
            'b': self.__bold,
            'i': self.__italic,
            'u': self.__underline,
            's': self.__strike,

            'bi': self.__bold_italic,
            'bu': self.__bold_under,
            'bs': self.__bold_strike,

            'iu': self.__italic_underline,
            'is': self.__italic_strike,

            'biu': self.__bold_italic_under,
            'bis': self.__bold_italic_strike,
        }

    def style(self, preset: str = None, string: str = None) -> str:
        return self.__data[preset].format(string)


class Emo:

    def __init__(self):
        self.top = emojize(":glowing_star:")
        self.wqm = emojize(":white_question_mark:")

        self.info = emojize(":information:")
        self.problem = emojize(":outbox_tray:")

        self.call = emojize(":telephone:")
        self.feed = emojize(":memo:")
        self.quest = emojize(":closed_book:")

        self.menu = emojize(":control_knobs:")

        self.cmb = emojize(":check_mark_button:")
        self.cm = emojize(":cross_mark:")


class Temp:
    def __init__(self):
        self.reformat = Format()
        self.smile = Emo()


edit = Temp()

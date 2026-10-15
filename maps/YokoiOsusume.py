from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "すき家の三種のチーズ牛丼"

    def get_summary(self):
        return "めっちゃチーズの味がして最高です。チーズ好きはぜひ"
        
    def get_author(self):
        return "横井"
from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "おすすめの学食メニューをここに書く"

    def get_summary(self):
        return "おすすめのポイント"
        
    def get_author(self):
        return "書いた人の名前"
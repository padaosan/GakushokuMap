from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "唐揚げ丼"

    def get_summary(self):
        return "愛和のメニューの中で、一番値段の割に腹が満たせる"
        
    def get_author(self):
        return "兵頭"
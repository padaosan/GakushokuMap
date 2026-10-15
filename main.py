from maps.GakushokuShota import GakushokuShota
from maps.hyodo_no_osusume import HyodoOsusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [HyodoOsusume() ,GakushokuShota()]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
from maps.GakushokuSample import GakushokuSample
from maps.GakushokuShota import GakushokuShota
from maps.Gakusyoku598410503Osusume import Gakusyoku598410503Osusume
from maps.hyodo_no_osusume import HyodoOsusume
from maps.YokoiOsusume import YokoiOsusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [
    GakushokuSample(),
    YokoiOsusume(),
    HyodoOsusume(),
    GakushokuShota(),
    Gakusyoku598410503Osusume(),
]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
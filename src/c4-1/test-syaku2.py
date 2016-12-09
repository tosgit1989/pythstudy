# ディレクトリにモジュールファイルが入っている場合、
# import (ディレクトリ名).(ファイル名(pyの拡張子はつけない))
import mod.modsyaku;

print("15尺=", mod.modsyaku.syaku_to_cm(15), "cm")
print("30尺=", mod.modsyaku.syaku_to_cm(30), "cm")
"""Corrections to the source, used by extract.py and compare.py and listed in NOTES.md.

Each Chinese fix is (section, source text, corrected text), with enough context to be unique in
that section once the source's stray spaces are dropped (the title of case 10 and the case share one). All are slips in the online transcription where the Taishō text (CBETA T48n2005)
has a character of similar shape that the sense, and Sekida's English, require. Differences of
reading between the Japanese edition and the Taishō are not here: they are kept as in the source.
"""

EN_FIXES = [("10", "Utterly Destitude", "Utterly Destitute")]   # case 10 title

ZH_FIXES = [
    ("preface", "貶得眼來", "眨得眼來"),   # "in the twinkling of an eye"
    ("1", "打成—片", "打成一片"),          # a dash for 一
    ("3", "倶胝堅指", "倶胝竪指"),          # title: "Gutei Raises a Finger"
    ("3", "童子亦堅指頭", "童子亦竪指頭"),
    ("3", "胝却堅起指", "胝却竪起指"),
    ("3", "童子興自己", "童子與自己"),      # "and you yourself"
    ("6", "惟迦葉者", "惟迦葉尊者"),        # 尊 missing
    ("6", "吾有正方眼藏", "吾有正法眼藏"),   # "the True Dharma Eye", four times
    ("6", "都笑、正方眼藏", "都笑、正法眼藏"),
    ("6", "不笑、正方眼藏", "不笑、正法眼藏"),
    ("6", "若道正方眼藏", "若道正法眼藏"),
    ("7", "其甲乍入", "某甲乍入"),          # "I have just entered"
    ("8", "去却輻", "去却軸"),              # "and the axle"
    ("9", "若知、既是聖人", "若知、即是聖人"),          # "he is a sage"
    ("9", "若會、既是凡夫", "若會、即是凡夫"),
    ("9", "更封候", "更封侯"),              # enfeoffed as a lord
    ("10", "清税弧貧", "清税孤貧"),          # title and case: "destitute" (applied to both)
    ("11", "主、堅起拳頭", "主、竪起拳頭"),      # "raised his fist", three times
    ("11", "主亦堅起拳頭", "主亦竪起拳頭"),
    ("11", "一般堅起拳頭", "一般竪起拳頭"),
    ("13", "若是未後句", "若是末後句"),      # "the last word"
    ("16", "隨聲遂色", "隨聲逐色"),          # "swayed by sounds and forms"
    ("21", "門挂戸", "門拄戸"),              # "to support"
    ("21", "撃石化", "撃石火"),              # spark from a flint
    ("21", "貶得眼", "眨得眼"),
    ("21", "巳蹉過", "已蹉過"),
    ("22", "呼弟鷹揚", "呼弟應揚"),          # "younger brother answers"
    ("23", "明白、我來", "明曰、我來"),   # "he cried"
    ("23", "明云、其申", "明云、某甲"),      # "I was with the monks"
    ("23", "無問曰", "無門曰"),      # Mumon's comment begins 無門曰
    ("26", "猶末合", "猶未合"),              # "does not come up to"
    ("28", "立君道", "立吾道"),              # "establish our Way"
    ("28", "瞎却眼晴", "瞎却眼睛"),          # "he lost his eyes"
    ("32", "氷綾上", "氷稜上"),              # an edge of ice
    ("38", "墮抗塹", "墮坑塹"),              # "falls into a ditch"
    ("40", "命之爲山", "命之爲開山"),        # 開 missing: made him the founder
    ("40", "重關欄不住", "重關攔不住"),      # "cannot stop"
    ("44", "我興你", "我與你"),              # "I will give you"
    ("48", "高高山頂、白浪", "高高山頂立、白浪"),  # 立 missing
]

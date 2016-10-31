from __future__ import unicode_literals

import json
import bumblebee.output

class i3bar(bumblebee.output.Output):
    def __init__(self):
        self._data = []
        self._previous_background = None

    def start(self):
        return json.dumps({ "version": 1 }) + "["

    def add(self, obj):
        theme = obj.theme()

        data = {
            u"full_text": "{}{}{}".format(theme.prefix(obj), obj.data(), theme.suffix(obj)),
            "color": theme.color(obj),
            "background": theme.background(obj),
        }
        if theme.default_separators(obj) == False:
            data["separator"] = False
            data["separator_block_width"] = 0
            if theme.separator(obj):
                self._data.append({
                    u"full_text": theme.separator(obj),
                    "color": theme.background(obj),
                    "background": self._previous_background,
                    "separator": False,
                    "separator_block_width": 0,
                })

        self._data.append(data)
        self._previous_background = theme.background(obj)

    def get(self):
        data = json.dumps(self._data)
        self._data = []
        return data + ","

    def stop(self):
        return "]"

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sublime
import sublime_plugin
import sys

# sys.path.append( 'bidi' )
try:

    # Python 3

    from .bidi.arabic_reshaper import reshape
    from .bidi.algorithm import get_display
except ValueError:

    # Python 2

    from bidi.arabic_reshaper import reshape
    from bidi.algorithm import get_display



class popupBidiPreview(sublime_plugin.EventListener):
    def on_selection_modified(self, view: sublime.View):
        selectionSet = view.sel()
        for selectionRegion in selectionSet:
            bidiStr = bidiRegion(selectionRegion, view)
            ch = view.substr(selectionRegion)
            if ('\u0600' <= ch <= '\u06FF' or '\u0750' <= ch <= '\u077F' or '\u08A0' <= ch <= '\u08FF' or '\uFB50' <= ch <= '\uFDFF' or '\uFE70' <= ch <= '\uFEFF' or '\U00010E60' <= ch <= '\U00010E7F' or '\U0001EE00' <= ch <= '\U0001EEFF'):
                view.show_popup(bidiStr, 200)


class popupBidiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selectionSet = self.view.sel()
        for selectionRegion in selectionSet:
            bidiStr = bidiRegion(selectionRegion, self.view)
            self.view.show_popup(bidiStr, 200)


def bidiRegion(region, view):
    txt = view.substr(region)
    reshaped_text = reshape(txt)
    bdiText = get_display(reshaped_text)
    return bdiText

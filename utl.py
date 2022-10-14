# -*- coding: UTF-8 -*-
class OacUtils:

    @staticmethod
    def escape(s, quote=True):
        """
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true (the default), the quotation mark
        characters, both double quote (") and single quote (') characters are also
        translated.
        """
        if s:
            s = s.replace("&", "&amp;")  # Must be done first!
            s = s.replace("<", "&lt;")
            s = s.replace(">", "&gt;")
            if quote:
                s = s.replace('"', "&quot;")
                s = s.replace('\'', "&#x27;")
        return s

from cudatext import *
from .lorem import *
from .dlg import *
import string

class Command:
    def run(self):
        res = dlg_lorem()
        if res is None: return
        n_count, s_type = res
        is_tags = s_type=='t'
        is_para = s_type in ['p', 't']
        
        text = gettext(n_count, is_para, is_tags)
        
        x0, y0, x1, y1 = ed.get_carets()[0] 
        ed.insert(x0, y0, text)
        
        msg = 'Inserted %d paragraphs' if is_para else 'Inserted %d sentences'
        msg_status(msg % n_count)

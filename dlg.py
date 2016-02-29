from cudatext import *

def dlg_lorem():
    '''
    Gets 2-tuple (n_count, s_type) or None
    s_type: 's' sentences, 'p' paragraphs, 't' paragraphs with tags
    '''
    
    dlg_w = 300
    dlg_h = 160
    id_opt_s = 0
    id_opt_p = 1
    id_opt_t = 2
    id_count = 4
    id_ok = 5
    
    c1 = chr(1)
    res = dlg_custom('Lorem Ipsum', dlg_w, dlg_h, '\n'.join([]
      +[c1.join(['type=radio', 'cap=&Sentences', 'val=1', 'pos=6,6,300,0'])]
      +[c1.join(['type=radio', 'cap=&Paragraphs', 'pos=6,28,300,0'])]
      +[c1.join(['type=radio', 'cap=Paragraphs with <p> &tags', 'pos=6,50,300,0'])]
      +[c1.join(['type=label', 'cap=&Count:', 'pos=6,74,300,0'])]
      +[c1.join(['type=spinedit', 'val=4', 'props=1,2000,1', 'pos=6,92,100,0'])]
      +[c1.join(['type=button', 'cap=&OK', 'props=1', 'pos=100,130,194,0'])]
      +[c1.join(['type=button', 'cap=Cancel', 'pos=200,130,294,0'])]
      ))
      
    if res is None: return
    (btn, text) = res
    if btn!=id_ok: return
    
    text = text.splitlines()
    n_count = int(text[id_count])
    s_type = 's' if text[id_opt_s]=='1' else \
             'p' if text[id_opt_p]=='1' else \
             't' if text[id_opt_t]=='1' else \
             '-'
    return (n_count, s_type)
